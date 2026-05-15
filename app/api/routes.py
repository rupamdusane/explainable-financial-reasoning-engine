from fastapi import APIRouter
from app.models.schemas import TextAnalysisRequest
from app.pipeline.orchestrator import analyze_text

router = APIRouter()

@router.post("/analyze")
def analyze_financial_text(request: TextAnalysisRequest):
    result = analyze_text(request.text)
    return result