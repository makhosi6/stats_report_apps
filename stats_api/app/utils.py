from datetime import datetime, timedelta

def get_time_filters():
    now = datetime.now()
    last_week = now - timedelta(weeks=1)
    last_month = now - timedelta(days=30)
    return now, last_week, last_month