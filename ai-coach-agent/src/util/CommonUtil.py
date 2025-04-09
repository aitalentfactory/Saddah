import uuid


def get_uuid():
    uuidStr = uuid.uuid4()
    return str(uuidStr)