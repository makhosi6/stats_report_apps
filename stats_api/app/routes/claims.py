from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app.models.all import DLClaim, db
from app.utils import get_time_filters

claims_bp = Blueprint('claims', __name__,  url_prefix='/api/stats/claims')

@claims_bp.route('/total', methods=['GET'])
def total_claims():
    offset = request.args.get('offset') or 20
    now, last_week, last_month = get_time_filters(); 
    total = DLClaim.query.count()
    claims_last_month = DLClaim.query.filter(DLClaim.date_entered >= last_month).count()
    return jsonify({
        "total_claims": total,
        "last_month": claims_last_month,
        "properties": [b.serialize() for b in DLClaim.query.limit(offset)]
    })
    
@claims_bp.route('/bytype', methods=['GET'])
def claims_by_type():
    offset = request.args.get('offset') or 20
    now, last_week, last_month = get_time_filters(); 
    total_policies = DLClaim.query.count()
    policies_last_month = DLClaim.query.filter(DLClaim.date_entered >= last_month).count()
    return jsonify({
        "total_claims": total_policies,
        "last_month": policies_last_month,
        "properties": [b.serialize() for b in DLClaim.query.limit(offset)]
    })

@claims_bp.route('/approved', methods=['GET'])
def approved_claims():
    approved = DLClaim.query.filter(DLClaim.status == 'approved').count()
    return jsonify({
        "approved_claims": approved
    })

@claims_bp.route('/rejected', methods=['GET'])
def rejected_claims():
    rejected = DLClaim.query.filter(DLClaim.status == 'rejected').count()
    return jsonify({
        "rejected_claims": rejected
    })


@claims_bp.route('/by-policy', methods=['GET'])
def claims_by_policy():
    results = db.session.query(DLClaim.dl_policy_id, db.func.count(DLClaim.id)).group_by(DLClaim.dl_policy_id).all()
    return jsonify({result[0]: result[1] for result in results})


@claims_bp.route('/by-benefit', methods=['GET'])
def claims_by_benefit():
    results = db.session.query(DLClaim.dl_benefit_id, db.func.count(DLClaim.id)).group_by(DLClaim.dl_benefit_id).all()
    return jsonify({result[0]: result[1] for result in results})


@claims_bp.route('/time-period', methods=['GET'])
def claims_time_period():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # Validate 
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    # 
    query = DLClaim.query
    if start_date:
        query = query.filter(DLClaim.date_entered >= start_date)
    if end_date:
        query = query.filter(DLClaim.date_entered <= end_date)

    claims = query.all()
    return jsonify({
        "total_claims": len(claims),
        "claims": [claim.serialize() for claim in claims]
    })


@claims_bp.route('/daily', methods=['GET'])
def claims_daily():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    # Validate 
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    # 
    query = db.session.query(db.func.date(DLClaim.date_entered), db.func.count(DLClaim.id))
    if start_date:
        query = query.filter(DLClaim.date_entered >= start_date)
    if end_date:
        query = query.filter(DLClaim.date_entered <= end_date)
    query = query.group_by(db.func.date(DLClaim.date_entered))

    results = query.all()
    return jsonify({result[0].strftime('%Y-%m-%d'): result[1] for result in results})


@claims_bp.route('/weekly', methods=['GET'])
def claims_weekly():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Validate
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    #
    query = db.session.query(db.func.yearweek(DLClaim.date_entered), db.func.count(DLClaim.id))
    if start_date:
        query = query.filter(DLClaim.date_entered >= start_date)
    if end_date:
        query = query.filter(DLClaim.date_entered <= end_date)
    query = query.group_by(db.func.yearweek(DLClaim.date_entered))

    results = query.all()
    return jsonify({result[0]: result[1] for result in results})


@claims_bp.route('/monthly', methods=['GET'])
def claims_monthly():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Validate
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    #
    query = db.session.query(db.func.date_format(DLClaim.date_entered, '%Y-%m'), db.func.count(DLClaim.id))
    if start_date:
        query = query.filter(DLClaim.date_entered >= start_date)
    if end_date:
        query = query.filter(DLClaim.date_entered <= end_date)
    query = query.group_by(db.func.date_format(DLClaim.date_entered, '%Y-%m'))

    results = query.all()
    return jsonify({result[0]: result[1] for result in results})