from fastapi import FastAPI

from routes.fault_routes import router as fault_router
from routes.energy_routes import router as energy_router

app = FastAPI(
    title="Smart HVAC Management System API",
    version="1.0.0"
)

app.include_router(fault_router)
app.include_router(energy_router)


@app.get("/")
def home():
    return {
        "message": "Smart HVAC Management System API is running successfully!"
    }