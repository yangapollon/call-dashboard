# Call Dashboard

A REST API for managing phone calls, built with FastAPI and Python.

## How to Run Locally

1. Clone the repository
```bash
   git clone https://github.com/yangapollon/call-dashboard
```
2. Create a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Start the server
```bash
   uvicorn src.app:app --reload
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /calls | Returns all non-archived calls |
| GET | /calls/{call_id} | Returns a single call by its ID |
| PATCH | /calls/{call_id}/archive | Archives a call by its ID |

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pytest