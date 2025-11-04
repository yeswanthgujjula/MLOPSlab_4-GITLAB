"""
Smart Calorie + Distance Analyzer
---------------------------------
A realistic calorie & distance calculator that supports walking,
running, and cycling based on MET formula, speed, distance, and weight.
"""

def calories_burned(activity: str, weight_kg: float, distance_km: float, speed_kmph: float) -> float:
    """
    Calculates calories burned based on activity, distance, and speed.
    Formula: Calories = MET × Weight(kg) × (Time(hr))
    """
    met_table = {
        "walking": 3.8,
        "running": 9.8,
        "cycling": 7.5
    }

    activity = activity.lower()
    if activity not in met_table:
        raise ValueError("Unsupported activity")

    if weight_kg <= 0 or distance_km <= 0 or speed_kmph <= 0:
        raise ValueError("Inputs must be positive numbers")

    time_hr = distance_km / speed_kmph
    calories = met_table[activity] * weight_kg * time_hr
    return round(calories, 2)


def total_summary(weight_kg: float, sessions: list) -> dict:
    """
    Accepts a list of (activity, distance_km, speed_kmph)
    Returns total calories and total time spent
    """
    total_cal = 0
    total_time = 0

    for act, dist, spd in sessions:
        total_cal += calories_burned(act, weight_kg, dist, spd)
        total_time += dist / spd

    return {
        "total_calories": round(total_cal, 2),
        "total_hours": round(total_time, 2)
    }
