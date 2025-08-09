def load_data():
    import pandas as pd
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    return iris.data, iris.target


def preprocess_data(X):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    return scaler.fit_transform(X)