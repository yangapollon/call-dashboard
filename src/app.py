from fastapi import FastAPI, HTTPException
from src.services import call_service

app = FastAPI()

@app.get("/calls")
def get_calls():
    return call_service.get_all_calls()

@app.get("/calls/{call_id}")
def get_call_by_id(call_id):
    call = call_service.get_call_by_id(call_id)
    if call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return call

@app.patch("/calls/{call_id}/archive")
def patch_call(call_id):
    call = call_service.archive_call(call_id)
    if call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return call
