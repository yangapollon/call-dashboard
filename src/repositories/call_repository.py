from src.data.calls import CALLS

def find_all():
    # returns all calls
    return CALLS

def find_by_id(call_id):
    # return call by id
    for call in CALLS:
        if call['id'] == str(call_id):
            return call
    return None

