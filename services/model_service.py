from models.schemas import ClientInput, PredictionOutput
from utils.load_model import load_model_and_threshold
import numpy as np

model, threshold = load_model_and_threshold()

def predict_risk(data: ClientInput) -> PredictionOutput:
    features = np.array([[
    data.totalDebtBOB,
    data.totalPendingDebtBOB,
    data.averagePaymentTime,
    data.paymentDelayRate,
    data.debtCount
]])


    prob = model.predict_proba(features)[0][1]
    prediction = int(prob >= threshold)

    return PredictionOutput(prediction=prediction, probability=round(prob, 4), threshold=threshold)
