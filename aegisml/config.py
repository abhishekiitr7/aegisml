import os

# Path to store baseline metrics for regression tests
BASELINE_DIR = os.path.join(os.path.dirname(__file__), "..", "baselines")

# Threshold for performance drop allowed before regression test fails
ACCURACY_THRESHOLD = 0.02  # 2%