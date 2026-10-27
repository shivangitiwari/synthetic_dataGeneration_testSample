# synthetic_dataGeneration_testSample

A small FastAPI starter project for building and exposing REST APIs.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive OpenAPI docs are at
`http://127.0.0.1:8000/docs` and the alternative API reference is at
`http://127.0.0.1:8000/redoc`.

Example requests:

```bash
curl http://127.0.0.1:8000/health
curl "http://127.0.0.1:8000/api/v1/hello?name=Sam"
```

## Test

```bash
pytest
```