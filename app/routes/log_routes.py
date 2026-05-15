from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.log_parser import analyze_logs

router = APIRouter()

# Health check endpoint
@router.get("/health")
def health_check():
    return {"status": "healthy"}


# Log analysis endpoint
@router.post("/analyze-logs")
async def analyze_log_file(file: UploadFile = File(...)):


    # Validate uploaded file type
    if not file.filename or not file.filename.endswith(".log"):
        raise HTTPException(
            status_code=400,
            detail="Only .log files are supported"
        )

    try:
        # Read uploaded file content
        content = await file.read()

        # Convert bytes to string
        log_content = content.decode("utf-8")

        # Analyze log content
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