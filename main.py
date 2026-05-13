from src.services import call_service

print(call_service.get_all_calls())
print(call_service.get_call_by_id(1))
print(call_service.archive_call(5))