def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]

    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num

    return (min, max)

# Test case 1
assert get_min_max([3, 6, 7, 1, 2, 4, 5, 9, 0, 8]) == (0, 9)

# Test case 2
assert get_min_max([-32, 1, -1, 4, 5, 9, 65, 8]) == (-32, 65)

# Test case 3
assert get_min_max([-6, -97, -1, -22, -42, -5, -9, -8]) == (-97, -1)