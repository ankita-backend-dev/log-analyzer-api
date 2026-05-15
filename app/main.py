from fastapi import FastAPI
from app.routes.log_routes import router

# Initialize FastAPI application
app = FastAPI(title="Log Analyzer API")

# Register API routes
app.include_router(router)


# Root endpoint
@app.get("/")
def home():
    return {"message": "Log Analyzer API is running"}