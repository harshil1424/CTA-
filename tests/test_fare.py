from src.fare_calculator import calculate_fare


def test_calculate_fare():
    assert calculate_fare(1, 3) == 4
    assert calculate_fare(2, 2) == 2
    assert calculate_fare(3, 5) == 4
