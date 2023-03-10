import uuid


def get_hex_uuid() -> str:
    return uuid.uuid4().hex
