from uuid import uuid4
import math
import time


def generate_uuid():
    return str(uuid4())


def get_current_timestamp():
    return math.floor(time.time())
