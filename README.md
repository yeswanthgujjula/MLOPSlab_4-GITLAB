# MLOps Lab 4 – Smart Calorie + Distance Analyzer (GIT Lab)

# 🧮 Smart Calorie Analyzer — MLOps Lab

## 📘 Project Summary
The **Smart Calorie Analyzer** calculates calories burned and total workout time for activities such as walking, running, and cycling using weight, speed, and distance as inputs.  
The core functions — `calories_burned()` and `total_summary()` — were tested with both **Pytest** and **Unittest** frameworks to ensure accuracy and robust handling of invalid inputs.  
To automate testing and ensure continuous validation, two **GitHub Actions** workflows were created (one for Pytest and one for Unittest) under `.github/workflows/`.  
Each workflow triggers automatically on every push to the `main` branch, installs dependencies, runs tests, and generates reports.  
Both pipelines were updated to the latest stable GitHub Actions versions (`checkout@v4`, `setup-python@v5`, and `upload-artifact@v4`) and executed successfully, confirming that all test cases passed.  
This lab demonstrates how analytical Python scripts can be integrated with **CI/CD pipelines** to achieve automation, reliability, and reproducibility in MLOps workflows.

---

## ⚙️ Features
- Calculates calories and total time across multiple activities  
- Validates inputs for unsupported activities and negative values  
- Includes both Pytest and Unittest for testing  
- Automates all testing through GitHub Actions CI/CD  
- Uses updated and secure GitHub workflow versions  

---

## 📁 Repository Structure

MLOps_Lab4/  
│  
├── src/  
│   └── smart_calorie_analyzer.py  
│  
├── test/  
│   ├── test_pytest.py  
│   └── test_unittest.py  
│  
├── workflows/  
│   ├── github_lab1_pytest_action.yml  
│   └── github_lab2_unittest_action.yml  
│  
├── data/  
├── requirements.txt  
└── README.md  

---

## ⚙️ Setup Instructions (Windows / PowerShell)

1. Create and activate a virtual environment  

       python -m venv lab_01
       .\lab_01\Scripts\Activate.ps1

2. Install dependencies  

       pip install -r requirements.txt

3. Run Pytest tests  

       pytest -v

4. Run Unittest tests  

       python -m unittest discover -s test -p "test_unittest.py" -v

---

## 🤖 Continuous Integration (GitHub Actions)

Both workflows run automatically whenever code is pushed to the repository or a pull request is opened.

| Workflow | File | Trigger | Command |
|----------|------|---------|---------|
| **Pytest** | `github_lab1_pytest_action.yml` | push / PR on `main` | `pytest --junitxml=pytest-report.xml` |
| **Unittest** | `github_lab2_unittest_action.yml` | push / PR on `main` | `python -m unittest discover -s test` |

The Pytest workflow also uploads the XML report as an artifact so test results can be inspected from the Actions UI.

---

## 🧮 Application Overview

The Smart Calorie + Distance Analyzer estimates calories burned using the standard MET formula:

Calories = MET × Weight(kg) × Time(hr)  
Time(hr) = Distance(km) / Speed(km/h)

Supported activities and example MET values:

| Activity | MET |
|----------|-----|
| Walking  | 3.8 |
| Running  | 9.8 |
| Cycling  | 7.5 |

### Main Functions

- `calories_burned(activity, weight_kg, distance_km, speed_kmph)`  
  Calculates calories burned for a single activity session. Validates the activity type and ensures all numeric inputs are positive.

- `total_summary(weight_kg, sessions)`  
  Accepts a list of sessions `(activity, distance_km, speed_kmph)` and returns:
  - `total_calories` – sum of calories across all sessions  
  - `total_hours` – total time spent across all activities  

Example usage:

    from src.smart_calorie_analyzer import calories_burned, total_summary

    # Single run
    cal = calories_burned("running", 70, 5, 10)
    print(f"Calories burned: {cal}")

    # Multiple activities in one day
    sessions = [("walking", 3, 5), ("cycling", 10, 20)]
    summary = total_summary(70, sessions)
    print(summary)

---

## ✅ Local Test Summary

| Framework | Test File | Status |
|----------|-----------|--------|
| **Pytest** | `test/test_pytest.py` | ✅ All tests pass locally |
| **Unittest** | `test/test_unittest.py` | ✅ All tests pass locally |

---

## 📊 GitHub Actions Status

After pushing the project, both workflows in the **Actions** tab complete successfully, confirming that the Smart Calorie + Distance Analyzer behaves as expected under automated CI.

---

### 👨‍💻 Author

**Name:** Yaswanth Kumar Reddy


