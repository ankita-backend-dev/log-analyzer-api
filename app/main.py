from fastapi import FastAPI
from app.routes.log_routes import router

app = FastAPI(title="Log Analyzer API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Log Analyzer API is running"}