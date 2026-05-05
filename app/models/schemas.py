from pydantic import BaseModel
from typing import List, Dict

class InputText(BaseModel):
    text: str
    
class Concept(BaseModel):
    term: str
    normalized: str
    category: str = None
    polarity: float = 0.0
    
class AnalysisResult(BaseModel):
    original_text: str
    concepts: List[Concept]
    overall_sentiment: float
    explanation: str
    