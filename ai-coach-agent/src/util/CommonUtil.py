import random
import uuid


def get_uuid():
    uuidStr = uuid.uuid4()
    return str(uuidStr)

def get_score():
    random_float = round(random.uniform(1, 10), 2)
    return random_float