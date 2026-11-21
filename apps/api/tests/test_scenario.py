import pytest
from fastapi.testclient import TestClient
from pathways.api.main import app
from pathways.domain.scenario import STAGES, evaluate_stage

client = TestClient(app)

def test_three_stages_are_bilingual():
    assert len(STAGES) == 3
    for stage in STAGES:
        assert stage["story"]["en"] and stage["story"]["zu"]
        assert len(stage["choices"]) == 3
        assert all(c["feedback"]["en"] and c["feedback"]["zu"] for c in stage["choices"])

def test_feedback_is_exploratory():
    result = evaluate_stage("investigate", "pipes")
    assert result["explore_career_id"] == "engineering"
    assert "does not measure" in result["note"]

@pytest.mark.parametrize("stage,choice", [("bad", "pipes"), ("investigate", "bad"), ("prioritize", "pipes")])
def test_invalid_combinations_rejected(stage, choice):
    with pytest.raises(ValueError):
        evaluate_stage(stage, choice)

def test_stage_endpoints():
    response = client.get("/v1/discovery/stages")
    assert response.status_code == 200
    assert len(response.json()["items"]) == 3
    result = client.post("/v1/discovery/stage-feedback", json={"stage_id":"review", "choice_id":"listen"})
    assert result.status_code == 200
    assert result.json()["explore_career_id"] == "community"

def test_stage_endpoint_rejects_invalid():
    assert client.post("/v1/discovery/stage-feedback", json={"stage_id":"review", "choice_id":"pipes"}).status_code == 422
