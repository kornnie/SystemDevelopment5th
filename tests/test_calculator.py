"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance for tests."""
    return Calculator()


TEST_MAX_VALUE = Calculator.MAX_VALUE
TEST_MIN_VALUE = Calculator.MIN_VALUE


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_first_arg_max_out_of_range(self, calc):
        """Test adding first argument as maximum out of range number."""
        # Arrange
        a = TEST_MAX_VALUE + 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_add_second_arg_max_out_of_range(self, calc):
        """Test adding second argument as maximum out of range number."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE + 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_add_first_arg_min_out_of_range(self, calc):
        """Test adding first argument as minimum out of range number."""
        # Arrange
        a = TEST_MIN_VALUE - 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_add_second_arg_min_out_of_range(self, calc):
        """Test adding second argument as minimum out of range number."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE - 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_add_first_arg_max_boundary(self, calc):
        """Test adding first argument as a maximum boundary number."""
        # Arrange
        a = TEST_MAX_VALUE
        b = 1
        expected = TEST_MAX_VALUE + 1

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_second_arg_max_boundary(self, calc):
        """Test adding second argument as a maximum boundary number."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE
        expected = 1 + TEST_MAX_VALUE

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_first_arg_min_boundary(self, calc):
        """Test adding first argument as a minimum boundary number."""
        # Arrange
        a = TEST_MIN_VALUE
        b = 1
        expected = TEST_MIN_VALUE + 1

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_second_arg_min_boundary(self, calc):
        """Test adding second argument as a minimum boundary number."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE
        expected = 1 + TEST_MIN_VALUE

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self, calc):
        """Test subtracting positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self, calc):
        """Test subtracting negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_with_zero(self, calc):
        """Test subtracting positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_with_positive(self, calc):
        """Test subtracting zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = -1.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_first_arg_max_out_of_range(self, calc):
        """Test subtracting first argument as maximum out of range number."""
        # Arrange
        a = TEST_MAX_VALUE + 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_subtract_second_arg_max_out_of_range(self, calc):
        """Test subtracting second argument as maximum out of range number."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE + 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_subtract_first_arg_min_out_of_range(self, calc):
        """Test subtracting first argument as minimum out of range number."""
        # Arrange
        a = TEST_MIN_VALUE - 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_subtract_second_arg_min_out_of_range(self, calc):
        """Test subtracting second argument as minimum out of range number."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE - 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_subtract_first_arg_max_boundary(self, calc):
        """Test subtracting with first argument at maximum valid boundary."""
        # Arrange
        a = TEST_MAX_VALUE
        b = 1
        expected = TEST_MAX_VALUE - 1

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_second_arg_max_boundary(self, calc):
        """Test subtracting with second argument at maximum valid boundary."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE
        expected = 1 - TEST_MAX_VALUE

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_first_arg_min_boundary(self, calc):
        """Test subtracting with first argument at minimum valid boundary."""
        # Arrange
        a = TEST_MIN_VALUE
        b = 1
        expected = TEST_MIN_VALUE - 1

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_second_arg_min_boundary(self, calc):
        """Test subtracting with second argument at minimum valid boundary."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE
        expected = 1 - TEST_MIN_VALUE

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self, calc):
        """Test multiplying positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self, calc):
        """Test multiplying negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero(self, calc):
        """Test multiplying zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 9.25

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_first_arg_max_out_of_range(self, calc):
        """Test multiplying first argument as maximum out of range number."""
        # Arrange
        a = TEST_MAX_VALUE + 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_multiply_second_arg_max_out_of_range(self, calc):
        """Test multiplying second argument as maximum out of range number."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE + 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_multiply_first_arg_min_out_of_range(self, calc):
        """Test multiplying first argument as minimum out of range number."""
        # Arrange
        a = TEST_MIN_VALUE - 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_multiply_second_arg_min_out_of_range(self, calc):
        """Test multiplying second argument as minimum out of range number."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE - 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_multiply_first_arg_max_boundary(self, calc):
        """Test multiplying with first argument at maximum valid boundary."""
        # Arrange
        a = TEST_MAX_VALUE
        b = 2
        expected = TEST_MAX_VALUE * 2

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_second_arg_max_boundary(self, calc):
        """Test multiplying with second argument at maximum valid boundary."""
        # Arrange
        a = 2
        b = TEST_MAX_VALUE
        expected = 2 * TEST_MAX_VALUE

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_first_arg_min_boundary(self, calc):
        """Test multiplying with first argument at minimum valid boundary."""
        # Arrange
        a = TEST_MIN_VALUE
        b = 2
        expected = TEST_MIN_VALUE * 2

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_second_arg_min_boundary(self, calc):
        """Test multiplying with second argument at minimum valid boundary."""
        # Arrange
        a = 2
        b = TEST_MIN_VALUE
        expected = 2 * TEST_MIN_VALUE

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing two positive numbers."""
        # Arrange
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_negative_numbers(self, calc):
        """Test dividing two negative numbers."""
        # Arrange
        a = -6
        b = -3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_positive_and_negative(self, calc):
        """Test dividing positive and negative numbers."""
        # Arrange
        a = 6
        b = -3
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_negative_and_positive(self, calc):
        """Test dividing negative and positive numbers."""
        # Arrange
        a = -6
        b = 3
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_zero_denominator(self, calc):
        """Test dividing positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = "Cannot divide by zero"

        # Act + Assert
        with pytest.raises(ValueError) as exc_info:
            calc.divide(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_divide_zero_nominator(self, calc):
        """Test dividing zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 0.67567567567567567567567567567568

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_first_arg_max_out_of_range(self, calc):
        """Test dividing first argument as maximum out of range number."""
        # Arrange
        a = TEST_MAX_VALUE + 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_divide_second_arg_max_out_of_range(self, calc):
        """Test dividing second argument as maximum out of range number."""
        # Arrange
        a = 1
        b = TEST_MAX_VALUE + 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_divide_first_arg_min_out_of_range(self, calc):
        """Test dividing first argument as minimum out of range number."""
        # Arrange
        a = TEST_MIN_VALUE - 1
        b = 1
        expected = (
            f"Input value {a} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_divide_second_arg_min_out_of_range(self, calc):
        """Test dividing second argument as minimum out of range number."""
        # Arrange
        a = 1
        b = TEST_MIN_VALUE - 1
        expected = (
            f"Input value {b} is outside the valid range "
            f"[{TEST_MIN_VALUE}, {TEST_MAX_VALUE}]"
        )

        # Act + Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(a, b)

        # Assert
        assert str(exc_info.value) == expected

    def test_divide_first_arg_max_boundary(self, calc):
        """Test dividing with first argument at maximum valid boundary."""
        # Arrange
        a = TEST_MAX_VALUE
        b = 2
        expected = TEST_MAX_VALUE / 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_second_arg_max_boundary(self, calc):
        """Test dividing with second argument at maximum valid boundary."""
        # Arrange
        a = 2
        b = TEST_MAX_VALUE
        expected = 2 / TEST_MAX_VALUE

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_first_arg_min_boundary(self, calc):
        """Test dividing with first argument at minimum valid boundary."""
        # Arrange
        a = TEST_MIN_VALUE
        b = 2
        expected = TEST_MIN_VALUE / 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_second_arg_min_boundary(self, calc):
        """Test dividing with second argument at minimum valid boundary."""
        # Arrange
        a = 2
        b = TEST_MIN_VALUE
        expected = 2 / TEST_MIN_VALUE

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)
