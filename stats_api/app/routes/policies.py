from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from app.models.all import DLPolicy, DLBranch, db
from app.utils import get_time_filters

policies_bp = Blueprint("policies", __name__, url_prefix="/api/stats/policies")


@policies_bp.route("/total", methods=["GET"])
def total_policies():
    offset = request.args.get('offset') or 20
    now, last_week, last_month = get_time_filters(); 
    total = DLPolicy.query.count()
    policies_last_month = DLPolicy.query.filter(DLPolicy.date_entered >= last_month).count()
    return jsonify(
        {
            "total_policies": total,
            "last_month": policies_last_month,
            "properties": [b.serialize() for b in DLPolicy.query.limit(offset)],
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


@policies_bp.route("/bytype", methods=["GET"])
def policies_by_type():
    return jsonify({})


@policies_bp.route("/time-period", methods=["GET"])
def policies_time_period():
    now, last_week, last_month = get_time_filters(); 
    policies_last_week = DLPolicy.query.filter(
        DLPolicy.date_entered >= last_week
    ).count()
    policies_last_month = DLPolicy.query.filter(
        DLPolicy.date_entered >= last_month
    ).count()
    return jsonify({"last_week": policies_last_week, "last_month": policies_last_month})


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


