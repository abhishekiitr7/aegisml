from aegisml.integration_tests import run_pipeline
import pandas as pd
import numpy as np
import pytest

@pytest.mark.parametrize("_", range(5))
def test_random_noise(_):
    noise = np.random.rand(5, 4) * 1000  # extreme values
    df = pd.DataFrame(noise, columns=["f1", "f2", "f3", "f4"])
    try:
        run_pipeline(df)
    except Exception as e:
        pytest.fail(f"Pipeline crashed with error: {e}")