"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
from timeit import default_timer as timer


def binary_search(input_array, value):
    left, right = 0, len(input_array) - 1

    while left <= right:
        mid = (left + right) // 2
        if input_array[mid] == value:
            return mid

        if value < input_array[mid]:
            right = mid - 1
        else:
            # value > input_array[mid]
            left = mid + 1

    return -1


if __name__ == '__main__':
    test_list = [0, 1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))
    print(binary_search(test_list, 0))
    print(binary_search(test_list, 30))

    beg = timer()
    for _ in range(10000):
        try:
            test_list.index(30)
        except ValueError as e:
            pass
    close = timer()
    builtin_search_time = (close - beg) / 10000
    beg = timer()
    for _ in range(10000):
        binary_search(test_list, 30)
    close = timer()
    binary_search_time = (close - beg) / 10000
    print('Average time taken for search: built-in={}s, binary={}s'.format(builtin_search_time, binary_search_time))
