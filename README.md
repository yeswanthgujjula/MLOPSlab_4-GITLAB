# MLOps Lab 1 – Smart Calorie + Distance Analyzer  

[![Pytest](https://github.com/<your-username>/MLOps_Lab3/actions/workflows/github_lab1_pytest_action.yml/badge.svg)](https://github.com/<your-username>/MLOps_Lab3/actions/workflows/github_lab1_pytest_action.yml)
[![Unittests](https://github.com/<your-username>/MLOps_Lab3/actions/workflows/github_lab2_unittest_action.yml/badge.svg)](https://github.com/<your-username>/MLOps_Lab3/actions/workflows/github_lab2_unittest_action.yml)

---

## 🔧 Changes Made in This Assignment

| Area | Description |
|------|-------------|
| **Application** | Replaced the default calculator example with `smart_calorie_analyzer.py`, which estimates calories burned from activity type, distance, speed and body weight using MET values. |
| **Testing** | Implemented both **Pytest** and **Unittest** suites in the `test/` folder to validate correct outputs, invalid inputs and edge cases. |
| **Automation** | Added two GitHub Actions workflows (`github_lab1_pytest_action.yml` and `github_lab2_unittest_action.yml`) that automatically run the test suites on every push. |
| **Enhancements** | Supports multiple real-world activities (Walking, Running, Cycling) and rejects unsupported activities or non-positive values. |
| **Documentation** | Created this README to describe setup, logic, testing and CI/CD integration for the lab. |

---

## 📁 Repository Structure

MLOps_Lab3/  
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

**Name:** Yash Gujjula  
**Course:** IE-7374 – MLOps  
**University:** George Mason University
