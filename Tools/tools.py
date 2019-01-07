from datetime import timedelta
from datetime import datetime

def datetime_offset_by_month(datetime1, n = 1):
    one_day = timedelta(days = 1)
    q,r = divmod(datetime1.month + n, 12)
    datetime2 = datetime(
        datetime1.year + q, r + 1, 1) - one_day

    if datetime1.month != (datetime1 + one_day).month:
        return datetime2
    
    if datetime1.day >= datetime2.day:
        return datetime2
    
    return datetime2.replace(day = datetime1.day)
 