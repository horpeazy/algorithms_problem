def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number
    such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first = 0
    second = 0
    sorted_list = merge_sort(input_list)
    for i in range(len(sorted_list) - 1, -1, -1):
        if i % 2 == 0:
            first = (first * 10) + sorted_list[i]
        else:
            second = (second * 10) + sorted_list[i]

    return [first, second]


def merge_sort(arr):
    """
    Sort an array of elements using divide and conquer algorithm.

    Args:
       arr(list): Input List
    Returns:
       (array): sorted array
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """
    Merge two arrays left and right

    Args:
    left(list), right(list): Left array and right array

    Returns:
    (array): merged array
    """
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output += left[i:]
    output += right[j:]

    return output


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
        return True
    else:
        print("Fail")
        return False


# Test case 1
assert test_function([[1, 2, 3, 4, 5], [542, 31]])
# >>> Pass

# Test case 2
assert test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# >>> Pass

# Test case 3
assert test_function([[2, 1, 8, 9, 3, 5], [952, 831]])
# >>> Pass
