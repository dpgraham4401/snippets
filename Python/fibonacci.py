# Given a number n, return the nth Fibonacci number.
import pytest


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    previous, current = 0, 1
    for _ in range(0, n - 1):
        previous, current = current, previous + current
    return current


def fibonacci_recursive(n: int):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


class TestFibonacciFunction:
    def test_returns_0_and_one(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    @pytest.mark.parametrize('input_number,expected_result', [(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)])
    def test_the_beginning_of_the_series(self, input_number, expected_result):
        assert fibonacci(input_number) == expected_result

    @pytest.mark.parametrize('input_number,expected_result', [(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)])
    def test_recursive_fibonacci_function(self, input_number, expected_result):
        assert fibonacci_recursive(input_number) == expected_result


if __name__ == '__main__':
    pytest.main(['-v', __file__])
