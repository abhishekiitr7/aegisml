from .utils import load_data, preprocess_data

def train_model():
    from sklearn.linear_model import LogisticRegression
    X, y = load_data()
    X_processed = preprocess_data(X)
    model = LogisticRegression(max_iter=200)
    model.fit(X_processed, y)
    return model