import joblib

def load_model_and_threshold():
    model = joblib.load("saved_model/model.pkl")
    threshold = 0.4 
    return model, threshold
