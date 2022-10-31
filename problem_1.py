def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    return sqrt_helper(0, number, number)


def sqrt_helper(lower_bound, upper_bound, target):
    """
    Recursive function to calculate the square root of a number

    Args:
        lower_bound(float): lower bound of the range
        upper_bound(float): upper bound of the range
    Returns:
        int: Floored Square root
    """
    middle = (upper_bound + lower_bound) / 2
    square = middle ** 2
    if square == target:              # base case
        return int((middle // 1))
    elif square > target:
        return sqrt_helper(lower_bound, middle, target)
    else:
        return sqrt_helper(middle, upper_bound, target)


# Test 1
assert sqrt(100) == 10

# Test 2
assert sqrt(0) == 0

# Test 3
assert sqrt(169) == 13
