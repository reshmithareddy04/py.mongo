# schemas/user.py

def serializeDict(a) -> dict:
    # Implementation of serializeDict
    return {str(key): value for key, value in a.items()}

def serializeList(entity) -> list:
    # Implementation of serializeList
    return [serializeDict(a) for a in entity]
