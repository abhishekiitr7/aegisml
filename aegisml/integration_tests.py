from .model_checks import train_model
from .utils import load_data, preprocess_data

def run_pipeline(X_input=None):
    model = train_model()
    if X_input is None:
        X, _ = load_data()
        X_input = X
    X_processed = preprocess_data(X_input)
    return model.predict(X_processed)