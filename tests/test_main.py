from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello_endpoint() -> None:
    response = client.get("/api/v1/hello", params={"name": "Sam"})

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Sam!"}