from app.models import DAGPayload
from datetime import timedelta

# Mock database to store DAGs data
mock_dags = {}

intervals = [
            None, "@once", "@hourly", "@daily", "@weekly", "@monthly", "@quarterly", "@yearly"
        ]

def validate_dag_data(dag_data: dict):
    """
    Validate the structure and content before storing it.
    """
    try:
        # Ensure the data conforms to the payload model
        DAGPayload(**dag_data)
        
        if not isinstance(dag_data["retry_delay"], timedelta):
            raise ValueError("retry_delay must be a timedelta object.")

        if dag_data["schedule_interval"] not in intervals and not isinstance(dag_data["schedule_interval"], str):
            raise ValueError("Invalid schedule interval format.")
        
        return True
    except Exception as e:
        raise ValueError(f"Invalid data: {e}")
