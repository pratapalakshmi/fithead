from uuid import uuid4
import math
import time
from datetime import datetime


def generate_uuid():
    return str(uuid4())


def get_current_timestamp():
    return math.floor(time.time())


def convert_date_string(date_string):
    """
    Convert a date string in DD-MM-YYYY format to a datetime.date object
    """
    return datetime.strptime(date_string, '%d-%m-%Y').date()
