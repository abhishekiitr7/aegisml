from aegisml.integration_tests import run_pipeline
from aegisml.utils import load_data

def test_full_pipeline_output_shape():
    X, _ = load_data()
    y_pred = run_pipeline(X)
    assert y_pred.shape[0] == X.shape[0]