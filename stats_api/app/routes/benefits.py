from datetime import datetime, timedelta
from flask import Blueprint, jsonify
from app.models.all import DLBenefit, db

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Hello World!"


benefits_bp = Blueprint('benefits', __name__, url_prefix='/api/stats/benefits')

@benefits_bp.route('/total', methods=['GET'])
def total_benefits():
    total = DLBenefit.query.count()
    last_month = DLBenefit.query.filter(DLBenefit.date_entered >= '2023-09-01').count()
    return jsonify({
        "total_benefits": total,
        "last_month": last_month,
        "properties": [b.serialize() for b in DLBenefit.query.limit(10)]
    })


@benefits_bp.route('/time-period', methods=['GET'])
def benefits_time_period():
    last_week = DLBenefit.query.filter(DLBenefit.date_entered >= datetime.now() - timedelta(days=7)).count()
    last_month = DLBenefit.query.filter(DLBenefit.date_entered >= datetime.now() - timedelta(days=30)).count()
    return jsonify({
        "last_week": last_week,
        "last_month": last_month
    })

@benefits_bp.route('/average-per-policy', methods=['GET'])
def average_benefits_per_policy():
    total_benefits = DLBenefit.query.count()
    total_policies = DLBenefit.query.with_entities(DLBenefit.policy_id).distinct().count()
    average = total_benefits / total_policies if total_policies > 0 else 0
    return jsonify({
        "average_benefits_per_policy": average
    })

@benefits_bp.route('/by-policy-type', methods=['GET'])
def benefits_by_policy_type():
    results = db.session.query(DLBenefit.type, db.func.count(DLBenefit.id)).group_by(DLBenefit.type).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/most-common', methods=['GET'])
def most_common_benefits():
    results = db.session.query(DLBenefit.name, db.func.count(DLBenefit.id)).group_by(DLBenefit.name).order_by(db.func.count(DLBenefit.id).desc()).limit(5).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/created-daily', methods=['GET'])
def benefits_created_daily():
    results = db.session.query(db.func.date(DLBenefit.date_entered), db.func.count(DLBenefit.id)).group_by(db.func.date(DLBenefit.date_entered)).all()
    return jsonify({result[0].strftime('%Y-%m-%d'): result[1] for result in results})

@benefits_bp.route('/created-weekly', methods=['GET'])
def benefits_created_weekly():
    results = db.session.query(db.func.yearweek(DLBenefit.date_entered), db.func.count(DLBenefit.id)).group_by(db.func.yearweek(DLBenefit.date_entered)).all()
    return jsonify({result[0]: result[1] for result in results})

@benefits_bp.route('/created-monthly', methods=['GET'])
def benefits_created_monthly():
    results = db.session.query(db.func.date_format(DLBenefit.date_entered, '%Y-%m'), db.func.count(DLBenefit.id)).group_by(db.func.date_format(DLBenefit.date_entered, '%Y-%m')).all()
    return jsonify({result[0]: result[1] for result in results})