from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_dag():
    response = client.post(
        "/dags",
        json={
            "dag_id": "test_id",
            "owner": "TestOwner",
            "description": "Test",
            "retries": 3,
            "retry_delay": 5,
            "start_date": "2023-12-01T00:00:00",
            "schedule_interval": "@daily",
            "catchup": False
        }
    )
    assert response.status_code == 200
    assert response.json()["dag_id"] == "test_id"

def test_get_dag_not_found():
    response = client.get("/dags/nonexistent_dag")
    assert response.status_code == 404


def test_create_dag_invalid_schedule_interval():
    response = client.post(
        "/dags",
        json={
            "dag_id": "invalid_dag",
            "owner": "TestOwner",
            "description": "An invalid test DAG",
            "retries": 3,
            "retry_delay": 5,
            "start_date": "2023-12-01T00:00:00",
            "schedule_interval": "invalid_schedule",
            "catchup": False
        }
    )
    assert response.status_code == 400
    assert "Invalid schedule_interval format." in response.json()["detail"]

def test_create_dag_invalid_retry_delay():
    response = client.post(
        "/dags",
        json={
            "dag_id": "invalid_dag_2",
            "owner": "TestOwner",
            "description": "An invalid test DAG",
            "retries": 3,
            "retry_delay": "invalid_value",
            "start_date": "2023-12-01T00:00:00",
            "schedule_interval": "@daily",
            "catchup": False
        }
    )
    assert response.status_code == 400
    assert "retry_delay must be a timedelta object." in response.json()["detail"]

def test_get_dag_with_data_issue():
    from app.database import mock_dags
    mock_dags["corrupted_dag"] = {
        "dag_id": "corrupted_dag",
        "owner": "TestOwner",
        "description": "A corrupted DAG",
        "retries": 3,
        "retry_delay": "invalid_value",
        "start_date": "2023-12-01T00:00:00",
        "schedule_interval": "@daily",
        "catchup": False
    }

    response = client.get("/dags/corrupted_dag")
    assert response.status_code == 500
    assert "Data integrity issue" in response.json()["detail"]