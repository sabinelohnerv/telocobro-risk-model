from pydantic import BaseModel

class ClientInput(BaseModel):
    totalDebtBOB: float
    totalPendingDebtBOB: float
    averagePaymentTime: float
    paymentDelayRate: float
    debtCount: int

class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    threshold: float
