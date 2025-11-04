import pytest
from src.smart_calorie_analyzer import calories_burned, total_summary

def test_calories_burned():
    assert calories_burned("walking", 70, 5, 5) == 266.0
    assert calories_burned("running", 70, 10, 10) == 686.0
    assert calories_burned("cycling", 70, 20, 20) == 525.0

def test_total_summary():
    activities = [("walking", 5, 5), ("running", 10, 10)]
    result = total_summary(70, activities)
    assert result["total_calories"] == 952.0
    assert round(result["total_hours"], 2) == 2.0


def test_invalid_activity():
    with pytest.raises(ValueError):
        calories_burned("jumping", 70, 5, 5)
