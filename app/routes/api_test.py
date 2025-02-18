from fastapi import APIRouter

router = APIRouter(prefix="/api_test", tags=["API TEST"])

@router.get("/")
async def health_check():
    return {"status": "ok"}