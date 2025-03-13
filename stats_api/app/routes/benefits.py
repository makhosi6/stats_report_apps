from datetime import datetime, timedelta

from sqlalchemy import func
from flask import Blueprint, jsonify, request
from app.models.all import DLBenefit, db
from app.utils import get_default_time_range, get_time_filters, parse_date_params

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Hello World!"


benefits_bp = Blueprint('benefits', __name__, url_prefix='/api/stats/benefits')
@benefits_bp.route('/total', methods=['GET'])
def total_benefits():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    total = DLBenefit.query.count()
    benefits_last_12_months = DLBenefit.query.filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).count()
    offset = int(request.args.get('offset', 20))
    return jsonify({
        "total_benefits": total,
        "benefits_last_12_months": benefits_last_12_months,
        "properties": [b.serialize() for b in DLBenefit.query.filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).limit(offset)]
    })

@benefits_bp.route('/time-period', methods=['GET'])
def benefits_time_period():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    benefits_count = DLBenefit.query.filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).count()

    return jsonify({
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "benefits_count": benefits_count
    })

@benefits_bp.route('/average-per-policy', methods=['GET'])
def average_benefits_per_policy():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    total_benefits = DLBenefit.query.filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).count()
    total_policies = DLBenefit.query.with_entities(DLBenefit.policy_id).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).distinct().count()
    average = total_benefits / total_policies if total_policies > 0 else 0

    return jsonify({
        "average_benefits_per_policy": average,
        "total_benefits": total_benefits,
        "total_policies": total_policies
    })

@benefits_bp.route('/by-policy-type', methods=['GET'])
def benefits_by_policy_type():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(DLBenefit.product_code, func.count(DLBenefit.id)).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).group_by(DLBenefit.product_code).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/most-common', methods=['GET'])
def most_common_benefits():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    offset = int(request.args.get('offset', 10))
    results = db.session.query(DLBenefit.name, func.count(DLBenefit.id)).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).group_by(DLBenefit.name).order_by(func.count(DLBenefit.id).desc()).limit(offset).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/created-daily', methods=['GET'])
def benefits_created_daily():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.date(DLBenefit.date_entered), func.count(DLBenefit.id)).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).group_by(func.date(DLBenefit.date_entered)).all()
    return jsonify({result[0].strftime('%Y-%m-%d'): result[1] for result in results})

@benefits_bp.route('/created-weekly', methods=['GET'])
def benefits_created_weekly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.yearweek(DLBenefit.date_entered), func.count(DLBenefit.id)).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).group_by(func.yearweek(DLBenefit.date_entered)).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/created-monthly', methods=['GET'])
def benefits_created_monthly():
    start_date, end_date, error = parse_date_params(request)
    if error:
        return jsonify(error), 400

    if not start_date or not end_date:
        start_date, end_date = get_default_time_range()

    results = db.session.query(func.date_format(DLBenefit.date_entered, '%Y-%m'), func.count(DLBenefit.id)).filter(DLBenefit.date_entered >= start_date, DLBenefit.date_entered <= end_date).group_by(func.date_format(DLBenefit.date_entered, '%Y-%m')).all()
    return jsonify({result[0]: result[1] for result in results})
