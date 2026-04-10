import pytest
from src.calculator import add, subtract, multiply, divide

class TestCloudCalculator:
    """Grouped test suite for Ominakavsar's calculator."""

    def test_addition_cases(self):
        assert add(100, 200) == 300.0
        assert add(-5, -5) == -10.0

    def test_subtraction_cases(self):
        assert subtract(50, 25) == 25.0
        assert subtract(1, 10) == -9.0

    def test_multiplication_cases(self):
        assert multiply(5, 5) == 25.0
        assert multiply(0, 100) == 0.0

    def test_division_cases(self):
        assert divide(100, 4) == 25.0
        assert divide(3, 2) == 1.5

    def test_error_handling(self):
        with pytest.raises(ValueError, match="Division by zero"):
            divide(1, 0)
