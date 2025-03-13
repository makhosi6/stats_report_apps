from datetime import datetime, timedelta

def get_time_filters():
    now = datetime.now()
    last_week = now - timedelta(weeks=1)
    last_month = now - timedelta(days=30)
    return now, last_week, last_month

def get_default_time_range():
    now = datetime.now()
    twelve_months_ago = now - timedelta(days=365)
    return twelve_months_ago, now

def parse_date_params(request):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    twelve_months_ago, now = get_default_time_range();
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d') if start_date else twelve_months_ago
        end_date = datetime.strptime(end_date, '%Y-%m-%d') if end_date else now
    except ValueError:
        return twelve_months_ago, now, {"error": "Invalid date format. Use YYYY-MM-DD."}
    return start_date, end_date, None
