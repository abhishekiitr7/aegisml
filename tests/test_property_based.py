from hypothesis import given, strategies as st
from aegisml.integration_tests import run_pipeline
import pandas as pd

@given(st.lists(st.floats(min_value=0, max_value=10), min_size=4, max_size=4))
def test_pipeline_does_not_crash(row_values):
    import numpy as np
    import pandas as pd
    df = pd.DataFrame([row_values], columns=["f1", "f2", "f3", "f4"])
    output = run_pipeline(df)
    assert output is not None