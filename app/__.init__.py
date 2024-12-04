from fastapi import FastAPI
from app.routes import router

# Initialize the FastAPI app
app = FastAPI(
    title="Mock DAG API",
    description="Mock implementation of an interface to create and manage DAGs.",
    version="1.0.0"
)

app.include_router(router)
