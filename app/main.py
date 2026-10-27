from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

app = FastAPI(title="Synthetic Data API", version="0.1.0")
api_router = APIRouter(prefix="/api/v1")


class MessageResponse(BaseModel):
    message: str


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@api_router.get("/hello", response_model=MessageResponse)
def hello(name: str = "world") -> MessageResponse:
    return MessageResponse(message=f"Hello, {name}!")


app.include_router(api_router)