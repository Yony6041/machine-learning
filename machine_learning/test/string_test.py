""" Module docstring: Tests for example functionality of pytest. """

# ! Delete this file once the first test is implemented


def reverse_string(sample_string: str):
    """Returns a string in reverse order

    Args:
        sample_string (str): Returns a string

    Returns:
        str: The string in reverse order
    """
    return sample_string[::-1]


def add(a_sample: int, b_sample: int) -> int:
    """Adds two numbers.

    Args:
        a_sample (int): The first number to add.
        b_sample (int): The second number to add.

    Returns:
        int: The sum of the two numbers.
    """
    return a_sample + b_sample


def test_reverse_string():
    """Test of reversing strings.

    This test will check if the reverse_string function correctly reverses
    various strings.
    """
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""  # Test with an empty string


def test_add_positive_numbers():
    """Test of adding two numbers.

    Args:
        a_sample (int): The first number to be tested in adding.
        b_sample (int): The second number to be tested in adding.

    Returns:
        int: The tests of the sum of the two numbers.
    """
    assert add(2, 3) == 5
    assert add(10, 15) == 25


test_reverse_string()
test_add_positive_numbers()
