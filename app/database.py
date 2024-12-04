from app.models import DAGPayload
from datetime import timedelta, datetime

# Mock database to store DAGs data
mock_dags = {}

intervals = [
            None, 
            "@once", 
            "@hourly", 
            "@daily", 
            "@weekly", 
            "@monthly", 
            "@quarterly", 
            "@yearly"
        ]

def validate_dag_data(dag_data: dict):
    """
    Validate the structure and content before storing it.
    """
    try:
        # Ensure the data conforms to the payload model
        DAGPayload(**dag_data)
        
        # Check if retry_delay is an integer
        if not isinstance(dag_data["retry_delay"], int):
            raise ValueError("retry_delay must be a valid integer.")

        # Validate schedule_interval
        if dag_data["schedule_interval"] not in intervals or not isinstance(dag_data["schedule_interval"], str):
            raise ValueError("Invalid schedule interval format.")
        
        # Ensure start_date is not in the past
        if dag_data["start_date"] < datetime.utcnow():
            raise ValueError("start_date cannot be in the past.")

        return True
    except Exception as e:
        raise ValueError(f"Invalid data: {e}")
