from sqlalchemy import func
from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app.models.all import DLPolicy, DLBenefit, DLBranch, db
from app.utils import get_time_filters, parse_date_params, get_default_time_range

policies_bp = Blueprint("policies", __name__, url_prefix="/api/stats/policies")
@policies_bp.route("/total", methods=["GET"])
def total_policies():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    total = DLPolicy.query.count()
    policies_last_12_months = DLPolicy.query.filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).count()
    offset = int(request.args.get('offset', 20))

    return jsonify({
        "total_policies": total,
        "policies_last_12_months": policies_last_12_months,
        "properties": [p.serialize() for p in DLPolicy.query.filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).limit(offset)]
    })

@policies_bp.route("/cancelled", methods=["GET"])
def cancelled_policies():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    cancelled = DLPolicy.query.filter(DLPolicy.policy_status == "cancelled", DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).count()
    return jsonify({"cancelled_policies": cancelled})

@policies_bp.route("/reinstated", methods=["GET"])
def reinstated_policies():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    reinstated = DLPolicy.query.filter(DLPolicy.policy_status == "reinstated", DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).count()
    return jsonify({"reinstated_policies": reinstated})

@policies_bp.route("/bytype", methods=["GET"])
def policies_by_type():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    results = db.session.query(DLPolicy.product_category, func.count(DLPolicy.id)).filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).group_by(DLPolicy.product_category).all()
    return jsonify({result[0]: result[1] for result in results})

@policies_bp.route("/time-period", methods=["GET"])
def policies_time_period():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    policies_count = DLPolicy.query.filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).count()
    return jsonify({
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "policies_count": policies_count
    })

@policies_bp.route("/by-premium", methods=["GET"])
def policies_by_premium():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    results = db.session.query(DLPolicy.premium, func.count(DLPolicy.id)).filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).group_by(DLPolicy.premium).all()
    return jsonify({result[0]: result[1] for result in results})

@policies_bp.route("/created-daily", methods=["GET"])
def policies_created_daily():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    results = db.session.query(func.date(DLPolicy.date_entered), func.count(DLPolicy.id)).filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).group_by(func.date(DLPolicy.date_entered)).all()
    return jsonify({result[0].strftime('%Y-%m-%d'): result[1] for result in results})

@policies_bp.route("/created-weekly", methods=["GET"])
def policies_created_weekly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    results = db.session.query(func.yearweek(DLPolicy.date_entered), func.count(DLPolicy.id)).filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).group_by(func.yearweek(DLPolicy.date_entered)).all()
    return jsonify({result[0]: result[1] for result in results})

@policies_bp.route("/created-monthly", methods=["GET"])
def policies_created_monthly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    results = db.session.query(func.date_format(DLPolicy.date_entered, '%Y-%m'), func.count(DLPolicy.id)).filter(DLPolicy.date_entered >= start_date, DLPolicy.date_entered <= end_date).group_by(func.date_format(DLPolicy.date_entered, '%Y-%m')).all()
    return jsonify({result[0]: result[1] for result in results})

@policies_bp.route("/average-benefits", methods=["GET"])
def average_benefits_per_policy():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400
    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()
    total_benefits = DLBenefit.query.filter(
        DLBenefit.date_entered >= start_date,
        DLBenefit.date_entered <= end_date
    ).count()
    total_policies = DLPolicy.query.filter(
        DLPolicy.date_entered >= start_date,
        DLPolicy.date_entered <= end_date
    ).count()
    average = total_benefits / total_policies if total_policies > 0 else 0
    return jsonify({
        "value": float(average),
        "total_benefits": total_benefits,
        "total_policies": total_policies,
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d')
    })

@policies_bp.route("/by-branch", methods=["GET"])
def policies_by_branch():
    results = (
        db.session.query(DLBranch.name, db.func.count(DLPolicy.dl_branch_id)).filter(DLPolicy.dl_branch_id == DLBranch.id)
        .group_by(DLBranch.name)
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/branch/<branchname>", methods=["GET"])
def policies_for_branch(branchname):
    current = DLPolicy.query.filter(DLBranch.name == branchname).first()
    policies = DLPolicy.query.filter(DLPolicy.dl_branch_id == current.id).all()
    return jsonify([p.serialize() for p in policies])


