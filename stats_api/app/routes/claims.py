from sqlalchemy import func
from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app.models.all import DLBenefit, DLClaim, db
from app.utils import get_default_time_range, get_time_filters, parse_date_params

claims_bp = Blueprint('claims', __name__,  url_prefix='/api/stats/claims')
@claims_bp.route('/total', methods=['GET'])
def total_claims():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    total = DLClaim.query.count()
    claims_last_12_months = DLClaim.query.filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).count()
    offset = int(request.args.get('offset', 20))

    return jsonify({
        "total_claims": total,
        "claims_last_12_months": claims_last_12_months,
        "properties": [c.serialize() for c in DLClaim.query.filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).limit(offset)]
    })

@claims_bp.route('/bytype', methods=['GET'])
def claims_by_type():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(DLClaim.claim_event, func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(DLClaim.claim_event).all()
    return jsonify({result[0]: result[1] for result in results})

@claims_bp.route('/approved', methods=['GET'])
def approved_claims():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    approved = DLClaim.query.filter(DLClaim.status == 'approved', DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).count()
    return jsonify({
        "approved_claims": approved
    })

@claims_bp.route('/rejected', methods=['GET'])
def rejected_claims():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    rejected = DLClaim.query.filter(DLClaim.status == 'rejected', DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).count()
    return jsonify({
        "rejected_claims": rejected
    })

@claims_bp.route('/by-policy', methods=['GET'])
def claims_by_policy():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(DLClaim.dl_policy_id, func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(DLClaim.dl_policy_id).all()
    return jsonify({result[0]: result[1] for result in results})

@claims_bp.route('/by-benefit', methods=['GET'])
def claims_by_benefit():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(DLClaim.dl_benefit_id, func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(DLClaim.dl_benefit_id).all()
    return jsonify({result[0]: result[1] for result in results})

@claims_bp.route('/time-period', methods=['GET'])
def claims_time_period():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    claims = DLClaim.query.filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).all()
    return jsonify({
        "total_claims": len(claims),
        "claims": [claim.serialize() for claim in claims]
    })

@claims_bp.route('/daily', methods=['GET'])
def claims_daily():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.date(DLClaim.date_entered), func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(func.date(DLClaim.date_entered)).all()
    return jsonify({result[0].strftime('%Y-%m-%d'): result[1] for result in results})

@claims_bp.route('/weekly', methods=['GET'])
def claims_weekly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.yearweek(DLClaim.date_entered), func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(func.yearweek(DLClaim.date_entered)).all()
    return jsonify({result[0]: result[1] for result in results})

@claims_bp.route('/monthly', methods=['GET'])
def claims_monthly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.date_format(DLClaim.date_entered, '%Y-%m'), func.count(DLClaim.id)).filter(DLClaim.date_entered >= start_date, DLClaim.date_entered <= end_date).group_by(func.date_format(DLClaim.date_entered, '%Y-%m')).all()
    return jsonify({result[0]: result[1] for result in results})