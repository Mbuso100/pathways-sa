"""Public response contracts are validated, not just HTTP status codes."""
from fastapi.testclient import TestClient
from pathways.api.main import app

client = TestClient(app)

def test_discovery_contracts():
    challenge = client.get('/v1/discovery/water-challenge')
    assert challenge.status_code == 200
    assert challenge.json()['choices'][0]['title']['zu']
    stages = client.get('/v1/discovery/stages')
    assert stages.status_code == 200
    assert len(stages.json()['items']) == 3
    for stage in stages.json()['items']:
        choice = stage['choices'][0]
        result = client.post('/v1/discovery/stage-feedback', json={'stage_id': stage['id'], 'choice_id': choice['id']})
        assert result.status_code == 200
        assert result.json()['feedback']['en']
        assert result.json()['feedback']['zu']

def test_invalid_stage_is_rejected():
    response = client.post('/v1/discovery/stage-feedback', json={'stage_id':'missing','choice_id':'missing'})
    assert response.status_code == 422

def test_resources_and_careers_contracts():
    for route in ('/v1/resources', '/v1/careers'):
        response = client.get(route)
        assert response.status_code == 200
        assert response.json()['items']
