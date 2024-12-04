from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta

class DAGPayload(BaseModel):
    dag_id: str
    description: Optional[str] = ""
    retries: int # In minute
    retry_delay: int 
    start_date: datetime
    schedule_interval: str
    catchup: bool

class DAGResponse(BaseModel):
    dag_id: str
    message: str
