from fastapi import APIRouter, Depends
from security.api_key import verify_api_key
from models.schemas import ClientInput, PredictionOutput
from services.model_service import predict_risk

router = APIRouter()

@router.post("/", response_model=PredictionOutput, dependencies=[Depends(verify_api_key)])
def predict(input_data: ClientInput):
    return predict_risk(input_data)
