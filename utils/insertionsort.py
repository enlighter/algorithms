def insertion_sort(array: list, desc: bool = False):
    n = len(array)
    array = array.copy()

    # array[0:1] subsection is always sorted by default, so 0th iteration is redundant here
    for i in range(1, n):
        item = array[i]
        j = i - 1
        if not desc:
            while j >= 0 and array[j] > item:
                # print('Looping, j=', j)
                array[j + 1] = array[j]
                j = j - 1
                # print(array)
        else:
            while j >= 0 and array[j] < item:
                # print('Looping, j=', j)
                array[j + 1] = array[j]
                j = j - 1
                # print(array)
        array[j+1] = item

    return array


if __name__ == '__main__':
    test_list = [3, 6, 8, 24, 7, 11, 16]
    sorted_list = insertion_sort(test_list, desc=True)
    print(sorted_list)
