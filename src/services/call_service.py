from src.repositories import call_repository

def get_all_calls():
    # return all non-archived calls from the in-memory store
    calls = call_repository.find_all()
    non_archived = [x for x in calls if not x["is_archived"]]
    return non_archived

def get_call_by_id(call_id):
    # return a single call with its notes, or None if not found
    call = call_repository.find_by_id(call_id)
    if call is None:
        return None
    call['notes'] = call.get('notes', [])
    return call

def archive_call(call_id):
    # set is_archived to True, return the updated call, or None if not found
    call = call_repository.find_by_id(call_id)
    if call is None:
        return None
    call['is_archived'] = True
    return call