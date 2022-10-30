def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1

    return rotated_binary_search(input_list, number, start_index, end_index)

def rotated_binary_search(arr, target, start, end):
    """
    Recursive function to search rotated sorted array

    Args:
        arr(array): Input array to search
        number(int): target to search for
        start_index(int): start index position
        end_index(int): end index position
    Returns:
        int: Index or -1
    """

    # base case
    if start > end:
        return -1

    mid = (start + end) // 2                            # mid index

    if arr[mid] == target:
        return mid
    elif target >= arr[start]:
        # if the end index element is less than target or mid index element is 
        # greater than target then the target could be on the left
        if arr[end] < target or arr[mid] > target:
            return rotated_binary_search(arr, target, start, mid-1)
        return rotated_binary_search(arr, target, mid + 1, end)
    else:
        return rotated_binary_search(arr, target, mid + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        return True
    else:
        return False

# Test case 1
assert test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

#Test case 2
assert test_function([[6, 7, 8, 1, 2, 3, 4], 8])

# Test 3
assert test_function([[6, 6, 6, 7, 8, 1, 2, 3, 4], 10])
