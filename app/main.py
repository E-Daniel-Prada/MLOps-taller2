from fastapi import FastAPI
from app.routes import predict, api_test

app = FastAPI(title="ML FastAPI Service")

app.include_router(predict.router)
app.include_router(api_test.router)

@app.get("/")
async def root():
    return {"message": "API de IA en FastAPI está funcionando"}