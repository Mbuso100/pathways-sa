from fastapi.testclient import TestClient
from pathways.api.main import app
from pathways.domain.discovery import reflect

client = TestClient(app)

def test_health():
    assert client.get('/health').json() == {'status':'ok'}

def test_choices_have_both_languages():
    response=client.get('/v1/discovery/water-challenge')
    assert response.status_code==200
    assert len(response.json()['choices'])==3
    for choice in response.json()['choices']:
        assert choice['title']['en'] and choice['title']['zu']

def test_reflection_does_not_assign_aptitude():
    result=client.post('/v1/discovery/reflections',json={'choice_id':'investigate'})
    assert result.status_code==200
    assert result.json()['explore_career_ids']==['engineering']
    assert 'not an aptitude' in result.json()['disclaimer']
    assert 'score' not in result.json()

def test_unknown_choice_rejected():
    assert client.post('/v1/discovery/reflections',json={'choice_id':'made-up'}).status_code==422

def test_resources_are_portals_not_open_listings():
    data=client.get('/v1/resources').json()
    assert data['status']=='source_portals_only'
    assert all(x['url'].startswith('https://') for x in data['items'])
    assert all('closing_date' not in x for x in data['items'])

def test_careers_are_exploration_only():
    assert client.get('/v1/careers').json()['status']=='illustrative_exploration_content'

def test_eligibility_remains_unverified_by_default():
    r=client.post('/v1/eligibility/evaluate',json={'highest_nqf_level':4,'minimum_nqf_level':4})
    assert r.json()['status']=='needs_verification'
