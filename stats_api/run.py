from flask import Flask, jsonify
import random
import calendar
from datetime import datetime, timedelta

app = Flask(__name__)

policy_types = [
    "WL_PC_25_EF",
    "WL_PC_25_CF",
    "WL_PM_CF",
    "WL_PM_EF",
    "WL_CLI_POPCRU",
    "LT_DI_AC",
    "WL_PC_25_ADMIN",
    "WL_PM_ADMIN",
    "WL_PG_ADMIN",
    "WL_PT_ADMIN",
    "WL_PP_ADMIN",
    "WL_PC_EX_EF",
    "WL_PG_CF",
    "WL_PP",
    "WL_PM",
    "WL_PP_EF",
    "WL_PC_ADD",
    "WL_PC_25_S_MEM",
    "WL_PG_EF",
    "WL_PT_EF",
    "WL_LP",
    "WL_PC",
    "WL_PC_25",
    "WL_PC_25_S",
    "WL_CH",
    "WL_CH_CF",
    "WL_PC_EF",
    "WL_PC_25_ADD",
    "WL_PC_ADMIN",
    "WL_PLAT_EF",
    "WL_PP_CF",
    "LT_DI_OM_AC",
    "WL_PM_S",
    "WL_COMP",
    "WL_COMP_CF",
    "WL_PC_CF",
    "WL_PM_ADD",
    "WL_PC_25_S_ADD",
    "WL_PC_S",
    "WL_CLI_PRESTIGE",
    "WL_PM_CF_ADD",
    "WL_PM_S_ADD",
    "WL_PG_ADD",
    "WL_PT_S",
    "WL_PP_ADD",
    "WL_COMP_EF",
    "WL_CH_EF",
    "WL_PC_25_MEM",
    "WL_PM_S_MEM",
    "WL_PP_S_ADD",
    "WL_PM_MEM",
    "WL_CLI_GOLD",
    "LT_DI_ACCEL",
]
branches = [
    "Harrismith",
    "Witbank",
    "Johannesburg",
    "Nelspruit",
    "Capetown",
    "Trigger",
    "Pietermaritzburg",
    "Klerksdorp",
    "Port Elizabeth",
    "Kokstad",
    "PGC House",
    "Claremont (Wynberg)",
    "George",
    "Mthatha",
    "Vanderbijl Park",
    "Rustenburg",
    "Queenstown",
    "Upington",
    "Newcastle",
    "IconAF",
    "Kimberly",
    "Polokwane",
    "Umthatha",
    "Empangeni",
    "Greytown",
    "Thohoyandou",
    "Smollan",
    "Bloemfontein",
    "East London",
    "Pretoria",
    "Mafikeng",
    "Durban",
]
premium_ranges = ["0-100", "101-500", "501-1000", "1001-2000", '2000+']
benefit_types = [
    "PM_LEGACY_1",
    "PM_GROUP_9",
    "PM_LEGACY_10",
    "PM_POPCRUB_2",
    "PM_POPCRUB_12",
    "PM_POPCRUB_8",
    "PM_POPCRUB_6",
    "PM_LEGACY_9",
    "PM_LEGACY_7",
    "PM_POPCRU2010_14",
    "PM_COMP_46",
    "PM_CHURCH_1",
    "PM_POPCRU25_16",
    "PM_EXTENDERB_7",
    "PM_POPCRU25_26",
    "PM_POPCRUB_10",
    "PM_EXTENDERB_11",
    "PM_POPCRUB_5",
    "PM_LEGACY_2",
    "PM_POPCRU25_28",
    "PM_LEGACY_8",
    "PM_PLAT_13",
    "PM_LEGACY_11",
    "LT_DI_OM_AC",
    "PM_COMP_17",
    "PM_EXTENDERB_1",
    "PM_EXTENDERP25_25",
    "PM_POPCRUGENY_29",
    "LP_POPCRU_0",
    "PM_EXTENDERB_8",
    "LP_COMPG_0",
    "PM_COMP_58",
    "PM_COMP_10",
    "PM_EXTENDERP25_27",
    "PM_COMP_14",
    "PM_CHURCH_7",
    "PM_POPCRUB_4",
    "PM_POPCRUB_3",
    "PM_LEGACY_5",
    "LP_COMPB_0",
    "PM_COMP_54",
    "PM_POPCRU25_27",
]
claim_statuses = ["Approved", "Rejected", "Pending", "Archived"]


def generate_time_series_data(days=30):
    """Generate time series data for the last `days` days."""
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days)]
    return {date: random.randint(1, 100) for date in dates}


# Policies Routes
@app.route("/api/stats/policies/total", methods=["GET"])
def total_policies():
    return jsonify({"total_policies": random.randint(1000, 5000)})


@app.route("/api/stats/policies/cancelled", methods=["GET"])
def cancelled_policies():
    return jsonify({"cancelled_policies": random.randint(50, 200)})


@app.route("/api/stats/policies/reinstated", methods=["GET"])
def reinstated_policies():
    return jsonify({"reinstated_policies": random.randint(10, 100)})


@app.route("/api/stats/policies/by-type", methods=["GET"])
def get_claim_data():
    return jsonify([
        {
            "amount": random.randint(100, 500),
            "status": random.choice(claim_statuses),
            "type": pt
        }
        for pt in policy_types
    ])

@app.route("/api/stats/policies/time-period", methods=["GET"])
def policies_time_period():
    return jsonify(generate_time_series_data())


@app.route("/api/stats/policies/by-premium", methods=["GET"])
def policies_by_premium():
    return jsonify({pr: random.randint(50, 300) for pr in premium_ranges})



@app.route("/api/stats/policies/created-daily", methods=["GET"])
def policies_created_daily():
    return jsonify(generate_time_series_data(7))


@app.route("/api/stats/policies/created-weekly", methods=["GET"])
def policies_created_weekly():
    return jsonify({f"Week {i+1}": random.randint(100, 300) for i in range(4)})


@app.route("/api/stats/policies/created-monthly", methods=["GET"])
def policies_created_monthly():
    return jsonify({i: random.randint(500, 1000) for i in list(calendar.month_name)[1:]})


@app.route("/api/stats/policies/by-branch", methods=["GET"])
def policies_by_branch():
    return jsonify({branch: random.randint(200, 600) for branch in branches})


@app.route("/api/stats/policies/branch/<branch>", methods=["GET"])
def policies_for_branch(branch):
    return jsonify({branch: random.randint(100, 400)})


# Benefits Routes
@app.route("/api/stats/benefits/total", methods=["GET"])
def total_benefits():
    return jsonify({"total_benefits": random.randint(5000, 10000)})


@app.route("/api/stats/benefits/time-period", methods=["GET"])
def benefits_time_period():
    return jsonify(generate_time_series_data())


@app.route("/api/stats/benefits/average-per-policy", methods=["GET"])
def average_benefits_per_policy():
    return jsonify({"average_benefits_per_policy": random.uniform(1.0, 5.0)})


@app.route("/api/stats/benefits/by-policy-type", methods=["GET"])
def benefits_by_policy_type():
    return jsonify({pt: random.randint(200, 800) for pt in policy_types})


@app.route("/api/stats/benefits/most-common", methods=["GET"])
def most_common_benefits():
    return jsonify({bt: random.randint(300, 700) for bt in benefit_types})


@app.route("/api/stats/benefits/created-daily", methods=["GET"])
def benefits_created_daily():
    return jsonify(generate_time_series_data(7))


@app.route("/api/stats/benefits/created-weekly", methods=["GET"])
def benefits_created_weekly():
    return jsonify({f"Week {i+1}": random.randint(200, 500) for i in range(4)})


@app.route("/api/stats/benefits/created-monthly", methods=["GET"])
def benefits_created_monthly():
    return jsonify({i: random.randint(500, 1000) for i in list(calendar.month_name)[1:]})


# Claims Routes
@app.route("/api/stats/claims/total", methods=["GET"])
def total_claims():
    return jsonify({"total_claims": random.randint(1000, 3000)})


@app.route("/api/stats/claims/approved", methods=["GET"])
def approved_claims():
    return jsonify({"approved_claims": random.randint(500, 1500)})


@app.route("/api/stats/claims/rejected", methods=["GET"])
def rejected_claims():
    return jsonify({"rejected_claims": random.randint(100, 500)})


@app.route("/api/stats/claims/by-policy", methods=["GET"])
def claims_by_policy():
    return jsonify({ pt: random.randint(100, 400) for pt in policy_types})


@app.route("/api/stats/claims/by-benefit", methods=["GET"])
def claims_by_benefit():
    return jsonify({bt: random.randint(50, 300) for bt in benefit_types})


@app.route("/api/stats/claims/time-period", methods=["GET"])
def claims_time_period():
    return jsonify(generate_time_series_data())


@app.route("/api/stats/claims/daily", methods=["GET"])
def claims_daily():
    return jsonify(generate_time_series_data(7))


@app.route("/api/stats/claims/weekly", methods=["GET"])
def claims_weekly():
    return jsonify({f"Week {i+1}": random.randint(100, 300) for i in range(4)})


@app.route("/api/stats/claims/monthly", methods=["GET"])
def claims_monthly():
    return jsonify({i: random.randint(500, 1000) for i in list(calendar.month_name)[1:]})


@app.route("/access", methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server", "server1")

    message = f"User {name} received access to server {server}"

    return jsonify({"Message": message})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
