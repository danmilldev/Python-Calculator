import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src.calculator import Calculator

import pytest

class TestCalculator:

    class TestSumFunction:
        def test_sum_correct_result(self):
            assert 3 == Calculator.sum(1,2)

        def test_sum_negative_values(self):
            assert -3 == Calculator.sum(-1,-2)

        def test_sum_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.sum('a','b')

    class TestDivideFunction:
        def test_divide_correct_result(self):
            assert 5 == Calculator.divide(10,2)

        def test_divide_negative_values(self):
            assert -3 == Calculator.divide(-9,3)

        def test_divide_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.divide('a','b')