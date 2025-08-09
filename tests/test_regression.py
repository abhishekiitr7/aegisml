import json
import os
from aegisml.config import BASELINE_DIR, ACCURACY_THRESHOLD
from aegisml.utils import load_data, preprocess_data
from aegisml.model_checks import train_model
from sklearn.metrics import accuracy_score

BASELINE_FILE = os.path.join(BASELINE_DIR, "baseline_metrics.json")

def test_model_accuracy_regression():
    X, y = load_data()
    model = train_model()
    acc = accuracy_score(y, model.predict(preprocess_data(X)))

    if not os.path.exists(BASELINE_FILE):
        os.makedirs(BASELINE_DIR, exist_ok=True)
        with open(BASELINE_FILE, "w") as f:
            json.dump({"accuracy": acc}, f)
    else:
        with open(BASELINE_FILE) as f:
            baseline = json.load(f)
        assert acc >= baseline["accuracy"] - ACCURACY_THRESHOLD, (
            f"Accuracy dropped from {baseline['accuracy']:.3f} to {acc:.3f}"
        )