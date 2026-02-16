"""
prime.py -- Write the application code here
"""
import pytest

def test_non_integer_raises_ValueError():
    with pytest.raises(ValueError):
        generate_prime_factors("A String")
    with pytest.raises(ValueError):
        generate_prime_factors(2.3)
    with pytest.raises(ValueError):
        generate_prime_factors([1,1])

def test_1_Returns_Empty_List():
    """Step 2: Assert that the number generates an Empty List[]"""
    assert generate_prime_factors(1) == []
def test_3_Returns_list_with_3():
    """Step 4: Assert that the number 3 generates a list with 3 [3]"""
    assert generate_prime_factors(3) == [3]

def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError('Input must be an integer')
    factors = []
    if n >1:
        while n % 2 == 0:
            factors.append(2)
            n //= 2
    return factors    divisor = 2

    while n >1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors
