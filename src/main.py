def calculate_square(number):
    return number * number
from src.main import calculate_square

def test_square_of_three_is_nine():
    assert calculate_square(3) == 9