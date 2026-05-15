from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.log_parser import analyze_logs

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/analyze-logs")
async def analyze_log_file(file: UploadFile = File(...)):

    if not file.filename or not file.filename.endswith(".log"):
        raise HTTPException(
            status_code=400,
            detail="Only .log files are supported"
        )

    try:
        content = await file.read()

        log_content = content.decode("utf-8")

        result = analyze_logs(log_content)

        return {
            "file_name": file.filename,
            "analysis": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing log file: {str(e)}"
        )