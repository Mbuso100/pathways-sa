from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathways.domain.eligibility import Applicant, OpportunityRequirements, assess
from pathways.domain.discovery import CHOICES, CAREERS, reflect
from pathways.domain.resources import RESOURCES
from pathways.domain.scenario import STAGES, evaluate_stage

app = FastAPI(title="Pathways SA API", version="0.3.0")
# Only local frontend development origins. Configure production origins explicitly before deployment.
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_methods=["GET", "POST"], allow_headers=["Content-Type"])

class EligibilityRequest(BaseModel):
    highest_nqf_level: int | None = Field(default=None, ge=1, le=10)
    province: str | None = None
    minimum_nqf_level: int | None = Field(default=None, ge=1, le=10)
    allowed_provinces: list[str] | None = None
    source_verified: bool = False

class StageRequest(BaseModel):
    stage_id: str = Field(min_length=1, max_length=40)
    choice_id: str = Field(min_length=1, max_length=40)

class ReflectionRequest(BaseModel):
    choice_id: str = Field(min_length=1, max_length=40)

class LocalizedText(BaseModel):
    en: str
    zu: str

class ChallengeChoice(BaseModel):
    id: str
    title: LocalizedText

class ChallengeResponse(BaseModel):
    id: str
    choices: list[ChallengeChoice]
    note: str

class StageChoiceResponse(BaseModel):
    id: str
    title: LocalizedText
    feedback: LocalizedText
    career_id: str

class StageResponse(BaseModel):
    id: str
    title: LocalizedText
    story: LocalizedText
    choices: list[StageChoiceResponse]

class StagesResponse(BaseModel):
    items: list[StageResponse]
    status: str

class StageFeedbackResponse(BaseModel):
    stage_id: str
    choice_id: str
    feedback: LocalizedText
    explore_career_id: str
    note: str

class ReflectionResponse(BaseModel):
    choice_id: str
    reflection: LocalizedText
    explore_career_ids: list[str]
    disclaimer: str

class CareerResponse(BaseModel):
    id: str
    title_en: str
    title_zu: str
    summary_en: str
    summary_zu: str

class CareersResponse(BaseModel):
    items: list[CareerResponse]
    status: str

class ResourceResponse(BaseModel):
    id: str
    name: str
    category: str
    url: str
    description_en: str
    description_zu: str

class ResourcesResponse(BaseModel):
    items: list[ResourceResponse]
    status: str
    warning: str

class EligibilityResponse(BaseModel):
    status: str
    reason_codes: list[str]

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/v1/discovery/water-challenge", response_model=ChallengeResponse)
def water_challenge() -> dict:
    return {"id":"water-challenge", "choices":[{"id":c.id,"title":{"en":c.en,"zu":c.zu}} for c in CHOICES], "note":"Fictional scenario, not a diagnostic test"}

@app.get("/v1/discovery/stages", response_model=StagesResponse)
def stages() -> dict:
    return {"items": list(STAGES), "status": "fictional_learning_activity"}

@app.post("/v1/discovery/stage-feedback", response_model=StageFeedbackResponse)
def stage_feedback(payload: StageRequest) -> dict:
    try:
        return evaluate_stage(payload.stage_id, payload.choice_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Unknown stage or choice") from None

@app.post("/v1/discovery/reflections", response_model=ReflectionResponse)
def reflection(payload: ReflectionRequest) -> dict:
    try:
        return reflect(payload.choice_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Unknown choice_id") from None

@app.get("/v1/careers", response_model=CareersResponse)
def careers() -> dict:
    return {"items":list(CAREERS), "status":"illustrative_exploration_content"}

@app.get("/v1/resources", response_model=ResourcesResponse)
def resources() -> dict:
    return {"items":list(RESOURCES), "status":"source_portals_only", "warning":"These are portals, not verified open applications. Check dates and requirements on the provider's site."}

@app.post("/v1/eligibility/evaluate", response_model=EligibilityResponse)
def evaluate(payload: EligibilityRequest) -> dict[str, object]:
    result = assess(Applicant(payload.highest_nqf_level, payload.province), OpportunityRequirements(payload.minimum_nqf_level, frozenset(p.upper() for p in payload.allowed_provinces) if payload.allowed_provinces is not None else None, payload.source_verified))
    return {"status":result.status.value,"reason_codes":list(result.reason_codes)}
