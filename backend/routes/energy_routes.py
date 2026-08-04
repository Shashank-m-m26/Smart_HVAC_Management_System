from fastapi import APIRouter

from schemas import EnergyPredictionRequest
from services.energy_service import predict_energy

router = APIRouter()


@router.post("/predict/energy")
def energy_prediction(request: EnergyPredictionRequest):

    result = predict_energy(request.model_dump())

    return result