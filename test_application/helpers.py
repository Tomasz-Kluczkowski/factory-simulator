from datetime import datetime


def get_drf_iso_date(date: datetime) -> str:
    """
    Returns datetime converted to a string in iso format the way django rest framework does it.
    """
    return date.isoformat().replace('+00:00', 'Z')
