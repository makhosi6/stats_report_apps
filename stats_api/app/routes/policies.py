from flask import Blueprint, jsonify
from datetime import datetime, timedelta
from app.models.all import DLPolicy, db

policies_bp = Blueprint("policies", __name__, url_prefix="/api/stats/policies")


@policies_bp.route("/total", methods=["GET"])
def total_policies():
    total = DLPolicy.query.count()
    last_month = DLPolicy.query.filter(DLPolicy.date_entered >= "2023-09-01").count()
    return jsonify(
        {
            "total_policies": total,
            "last_month": last_month,
            "properties": [b.serialize() for b in DLPolicy.query.limit(10)],
        }
    )


@policies_bp.route("/cancelled", methods=["GET"])
def cancelled_policies():
    cancelled = DLPolicy.query.filter(DLPolicy.policy_status == "cancelled").count()
    return jsonify({"cancelled_policies": cancelled})


@policies_bp.route("/reinstated", methods=["GET"])
def reinstated_policies():
    reinstated = DLPolicy.query.filter(DLPolicy.policy_status == "reinstated").count()
    return jsonify({"reinstated_policies": reinstated})


@policies_bp.route("/by-type", methods=["GET"])
def policies_by_type():
    results = (
        db.session.query(DLPolicy.policy_plan_code, db.func.count(DLPolicy.id))
        .group_by(DLPolicy.policy_plan_code)
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/time-period", methods=["GET"])
def policies_time_period():
    last_week = DLPolicy.query.filter(
        DLPolicy.date_entered >= datetime.now() - timedelta(days=7)
    ).count()
    last_month = DLPolicy.query.filter(
        DLPolicy.date_entered >= datetime.now() - timedelta(days=30)
    ).count()
    return jsonify({"last_week": last_week, "last_month": last_month})


@policies_bp.route("/by-premium", methods=["GET"])
def policies_by_premium():
    results = (
        db.session.query(DLPolicy.premium, db.func.count(DLPolicy.id))
        .group_by(DLPolicy.premium)
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/created-daily", methods=["GET"])
def policies_created_daily():
    results = (
        db.session.query(
            db.func.date(DLPolicy.date_entered), db.func.count(DLPolicy.id)
        )
        .group_by(db.func.date(DLPolicy.date_entered))
        .all()
    )
    return jsonify({result[0].strftime("%Y-%m-%d"): result[1] for result in results})


@policies_bp.route("/created-weekly", methods=["GET"])
def policies_created_weekly():
    results = (
        db.session.query(
            db.func.yearweek(DLPolicy.date_entered), db.func.count(DLPolicy.id)
        )
        .group_by(db.func.yearweek(DLPolicy.date_entered))
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/created-monthly", methods=["GET"])
def policies_created_monthly():
    results = (
        db.session.query(
            db.func.date_format(DLPolicy.date_entered, "%Y-%m"),
            db.func.count(DLPolicy.id),
        )
        .group_by(db.func.date_format(DLPolicy.date_entered, "%Y-%m"))
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/by-branch", methods=["GET"])
def policies_by_branch():
    results = (
        db.session.query(DLPolicy.dl_branch_id, db.func.count(DLPolicy.id))
        .group_by(DLPolicy.dl_branch_id)
        .all()
    )
    return jsonify({result[0]: result[1] for result in results})


@policies_bp.route("/branch/<branch>", methods=["GET"])
def policies_for_branch(branch):
    policies = DLPolicy.query.filter(DLPolicy.dl_branch_id == branch).all()
    return jsonify([p.serialize() for p in policies])
