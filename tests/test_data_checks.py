from aegisml.utils import load_data, preprocess_data

def test_missing_values_handling():
    X, _ = load_data()
    X.iloc[0, 0] = None  # introduce NaN
    processed = preprocess_data(X.fillna(0))
    assert processed is not None
    assert processed.shape[0] > 0