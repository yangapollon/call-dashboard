from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_calls():
    response = client.get("/calls")

    assert response.status_code == 200
    assert "calls" in response.json()

def test_get_call_by_id():
    response = client.get("/calls/1")

    assert response.status_code == 200
    assert response.json()["id"] == "1"

def test_get_call_by_id_not_found():
    response = client.get("/calls/888")

    assert response.status_code == 404

def test_archive_call():
    response = client.patch("/calls/2/archive")

    assert response.status_code == 200
    assert response.json()["is_archived"] == True

def test_archive_call_not_found():
    response = client.patch("/calls/888/archive")

    assert response.status_code == 404