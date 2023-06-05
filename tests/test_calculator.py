import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src.calculator import Calculator

import pytest

class TestCalculator:

    class TestSumFunction:
        def test_sum_correct_result(self):
            assert 3 == Calculator.sum(1, 2)

        def test_sum_negative_values(self):
            assert -3 == Calculator.sum(-1, -2)

        def test_sum_decimal_values(self):
            assert 0.3 == Calculator.sum(0.1, 0.2)

        def test_big_values(self):
            assert 999_999_999_999_999_999_999_999_999_999_999 == Calculator.sum(666_666_666_666_666_666_666_666_666_666_666,
                                                                                333_333_333_333_333_333_333_333_333_333_333)

        def test_sum_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.sum('a', 'b')

        def test_sum_invalid_first_value(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.sum(2, 'b')

        def test_sum_invalid_second_value(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.sum('a', 2)

    class TestDivideFunction:
        def test_divide_correct_result(self):
            assert 5 == Calculator.divide(10, 2)

        def test_divide_negative_values(self):
            assert -3 == Calculator.divide(-9, 3)

        def test_divide_decimal_values(self):
            assert 3 == Calculator.divide(0.9, 0.3)

        def test_big_values(self):
            assert 133_333_333_333_333_333_333_333_333_333_333_2 == Calculator.sum(999_999_999_999_999_999_999_999_999_999_999,
                                                                                    333_333_333_333_333_333_333_333_333_333_333)

        def test_divide_by_zero(self):
            with pytest.raises(ZeroDivisionError, match="division by zero"):
                Calculator.divide(999, 0)

        def test_divide_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.divide('a', 'b')

        def test_divide_invalid_first_value(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.divide('a', 2)

        def test_divide_invalid_second_value(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.divide(2, 'b')

    class TestMultiplyFunction:
        def test_correct_result(self):
            assert 100 == Calculator.multiply(25, 4)

        def test_negative_values(self):
            assert -100 == Calculator.multiply(-25, 4)

        def test_decmial_values(self):
            assert 99.99 == Calculator.multiply(33.33, 3)

        def test_big_values(self):
            assert 999_999_999_999_999_999_999_999_999_999_999 == Calculator.multiply(333_333_333_333_333_333_333_333_333_333_333,
                                                                                    3)

        def test_multiply_by_zero(self):
            assert 0 == Calculator.multiply(100, 0)

        def test_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.multiply('a', 'b')

        def test_invalid_first_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.multiply('a', 2)

        def test_invalid_second_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.multiply(2, 'b')

    class TestSubtractFunction:
        def test_correct_result(self):
            assert 20 == Calculator.subtract(100, 80)

        def test_nagetive_values(self):
            assert -20 == Calculator.subtract(-100, -80)

        def test_decimal_values(self):
            assert 40.5 == Calculator.subtract(100, 59.5)

        def test_big_values(self):
            assert 555_555_555_555_555_555_555_555_555_555_555 == Calculator.subtract(999_999_999_999_999_999_999_999_999_999_999,
                                                                                      444_444_444_444_444_444_444_444_444_444_444)

        def test_invalid_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.subtract('a', 'b')

        def test_invalid_first_value(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.subtract('a', 2)

        def test_invalid_second_values(self):
            with pytest.raises(TypeError, match="thats not a number."):
                Calculator.subtract(2, 'b')