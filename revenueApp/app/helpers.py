from django.db.models.functions import TruncHour, TruncDay

def get_annotate_by_duration(path):
    """
        Return the Truncation based on given time duration
    """
    if path.startswith('/sales/daily'):
        return TruncDay('updated_date')
    elif path.startswith('/saled/hourly'):
        return TruncHour('updated_date')
    return None