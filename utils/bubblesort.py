def bubble_sort(array: list, desc: bool = False):
    swapped = True
    n = len(array)
    array = array.copy()

    def _swap(pos1, pos2):
        t = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = t
        return True

    while swapped:
        print('Looping, n=', n)
        swapped = False
        for i in range(n-1):
            if array[i] > array[i+1]:
                swapped = _swap(i, i+1)
        n = n-1

    if desc:
        array = array[::-1]

    return array


if __name__ == '__main__':
    test_list = [3, 6, 7, 24, 8, 11, 16]
    sorted_list = bubble_sort(test_list)
    print(sorted_list)
