# =============================================================
#  MODULE 19 — TESTING
#  Level: [ERR] Expert
#  Goal:  unittest, pytest patterns, mocking, TDD.
#  Run:   python -m pytest main.py -v  (after pip install pytest)
# =============================================================

import unittest
from unittest.mock import patch, MagicMock

print("=" * 55)
print("  MODULE 19 — TESTING")
print("=" * 55)

# ---- Code to test ----

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def get_user_greeting(name):
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")
    return f"Hello, {name.strip().title()}!"

# ---- TESTS ----

class TestMathFunctions(unittest.TestCase):
    """Test our math functions."""

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestStringFunctions(unittest.TestCase):
    """Test string utilities."""

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_greeting_normal(self):
        self.assertEqual(get_user_greeting("alice"), "Hello, Alice!")

    def test_greeting_empty(self):
        with self.assertRaises(ValueError):
            get_user_greeting("")

    def test_greeting_whitespace(self):
        with self.assertRaises(ValueError):
            get_user_greeting("   ")


# ---- MOCKING EXAMPLE ----

def fetch_temperature(city):
    """Simulates an API call."""
    # In real code this would call an API
    raise NotImplementedError("Real API not available")

def weather_report(city):
    temp = fetch_temperature(city)
    if temp > 30:
        return f"{city}: Hot ({temp}°C)"
    return f"{city}: Pleasant ({temp}°C)"


class TestWeatherWithMock(unittest.TestCase):
    """Demonstrate mocking external dependencies."""

    @patch("__main__.fetch_temperature", return_value=35)
    def test_hot_weather(self, mock_fetch):
        result = weather_report("Delhi")
        self.assertIn("Hot", result)
        mock_fetch.assert_called_once_with("Delhi")

    @patch("__main__.fetch_temperature", return_value=22)
    def test_pleasant_weather(self, mock_fetch):
        result = weather_report("Shimla")
        self.assertIn("Pleasant", result)


# ---- Run Tests & Print Summary ----

if __name__ == "__main__":
    print("\n--- Running Tests ---\n")

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestMathFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestStringFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestWeatherWithMock))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print(f"\n  Total: {result.testsRun}")
    print(f"  [OK] Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"  [X] Failed: {len(result.failures)}")
    print(f"  [!] Errors: {len(result.errors)}")

    print("\n" + "=" * 55)
    print("  [TROPHY] CHALLENGES")
    print("=" * 55)
    print("  1. Write tests for a calculator class (TDD style)")
    print("  2. Test file I/O with temporary files")
    print("  3. Mock an API response and test error handling")
    print("=" * 55)
