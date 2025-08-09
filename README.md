# 🛡️ AegisML - AI Model Testing Toolkit

![Build Status](https://github.com/abhishekiitr7/aegisml/actions/workflows/ci.yml/badge.svg)
![Coverage](https://codecov.io/gh/abhishekiitr7/aegisml/branch/main/graph/badge.svg)
![License](https://img.shields.io/github/license/abhishekiitr7/aegisml)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)

AegisML is an open-source Python toolkit that automates **testing of AI/ML pipelines** for:
- ✅ **Correctness** – Are outputs as expected?
- ✅ **Reproducibility** – Do results remain consistent across runs?
- ✅ **Performance regression** – Did accuracy drop after code changes?
- ✅ **Robustness** – Does the pipeline handle malformed or extreme inputs?

This framework is designed for data scientists, ML engineers, and AI researchers who need **reliable, maintainable test suites** for complex machine learning systems.

---

## 📂 Project Structure

```
aegisml/
│── aegisml/
│   ├── config.py              # Global settings
│   ├── utils.py               # Data loading & preprocessing
│   ├── model_checks.py        # Unit tests for model methods
│   ├── integration_tests.py   # End-to-end inference checks
│
│── examples/
│   ├── example_pipeline.py    # Sample ML workflow
│
│── tests/
│   ├── test_data_checks.py    # Data preprocessing tests
│   ├── test_integration.py    # Integration tests
│   ├── test_property_based.py # Hypothesis-based stability tests
│   ├── test_regression.py     # Accuracy regression tests
│   ├── test_fuzz.py           # Robustness fuzz tests
│
│── .github/workflows/ci.yml   # GitHub Actions CI/CD pipeline
│── requirements.txt           # Dependencies
│── setup.py                   # Packaging setup
│── LICENSE
│── README.md
```

---

## Quickstart

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run tests
```bash
pytest --cov=aegisml
```

### 3️⃣ Check coverage report
```bash
coverage html
open htmlcov/index.html
```

---

## 🧪 Types of Tests

### **1. Unit Tests for Data Preprocessing**
Ensures preprocessing handles missing values, scaling, and transformations correctly.

### **2. Integration Tests**
Validates the **entire ML pipeline** from raw input → prediction output.

### **3. Property-Based Tests** (`hypothesis`)
Generates random valid data to ensure stability under varied inputs.

### **4. Regression Tests**
Compares new model performance against stored **baseline metrics**.

### **5. Fuzz Tests**
Pushes corrupted/extreme inputs to check robustness.

---

## 🔄 Continuous Integration (CI/CD)
Every push or pull request triggers:
- ✅ Automated tests via **pytest**
- ✅ Coverage reporting via **Codecov**
- ✅ Status badges updated in README

---

## 📊 Example Workflow

1. **Modify the model** in `model_checks.py`
2. **Run tests**:
```bash
pytest
```
3. If performance drops below threshold → regression test fails.
4. Fix issues before merging.

---

## 🏆 Why This Project Stands Out
- Covers **entire AI pipeline** testing.
- Combines **classical testing** + **ML-specific checks**.
- Uses **Hypothesis** for advanced property-based testing.
- Built with **professional CI/CD integration**.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact
**Author:** Abhishek Pal  
**GitHub:** [abhishekiitr7](https://github.com/abhishekiitr7)  
**Email:** abhishekiitr7@gmail.com

