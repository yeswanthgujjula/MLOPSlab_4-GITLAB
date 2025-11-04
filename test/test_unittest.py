import unittest
from src.smart_calorie_analyzer import calories_burned, total_summary

class TestSmartCalorie(unittest.TestCase):

    def test_calories(self):
        self.assertEqual(calories_burned("walking", 70, 5, 5), 266.0)
        self.assertEqual(calories_burned("running", 70, 10, 10), 686.0)

    def test_summary(self):
        data = [("walking", 5, 5), ("cycling", 20, 20)]
        res = total_summary(70, data)
        self.assertAlmostEqual(res["total_calories"], 791.0, places=1)
        self.assertAlmostEqual(res["total_hours"], 2.0, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calories_burned("jumping", 70, 5, 5)

if __name__ == '__main__':
    unittest.main()
