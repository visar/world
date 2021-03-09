import uuid


def gen_id():
    return int(str(uuid.uuid4().int)[:8])
