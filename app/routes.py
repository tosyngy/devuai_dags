from fastapi import APIRouter, HTTPException
from datetime import timedelta
from app.models import DAGPayload, DAGResponse
from app.database import mock_dags, validate_dag_data

router = APIRouter()

@router.post("/dags", response_model=DAGResponse)
async def create_dag(payload: DAGPayload):
    """
    Create a DAG.
    """
    if payload.dag_id in mock_dags:
        raise HTTPException(
            status_code=400, detail=f"DAG with ID '{payload.dag_id}' already exists."
        )

    # Convert retry_delay to timedelta for consistency
    payload_dict = payload.model_dump()
    # payload_dict["retry_delay"] = timedelta(minutes=payload.retry_delay)

    # Validate the DAG data before storing
    try:
        validate_dag_data(payload_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Store payload in database
    mock_dags[payload.dag_id] = payload_dict

    return DAGResponse(dag_id=payload.dag_id, message="DAG created successfully!")

@router.get("/dags/{dag_id}")
async def get_dag(dag_id: str):
    """
    Retrieve a DAG.
    """
    if dag_id not in mock_dags:
        raise HTTPException(status_code=404, detail=f"DAG with ID '{dag_id}' not found.")
    
    # Validate data before returning (ensures data integrity)
    try:
        validate_dag_data(mock_dags[dag_id])
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Data integrity issue: {e}")
    
    return mock_dags[dag_id]
