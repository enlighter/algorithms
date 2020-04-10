def bubble_sort(array: list, desc: bool = False):
    n = len(array)
    array = array.copy()

    def _swap(pos1, pos2):
        t = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = t
        return True

    while n > 1:
        # print('Looping, comparisons=', n-1)
        new_n = 0
        for i in range(n-1):
            if not desc:
                if array[i] > array[i+1]:
                    _swap(i, i+1)
                    new_n = i+1
            else:
                if array[i] < array[i+1]:
                    _swap(i, i+1)
                    new_n = i+1
        n = new_n
        # print(array)

    return array


if __name__ == '__main__':
    test_list = [3, 6, 8, 24, 7, 11, 16]
    sorted_list = bubble_sort(test_list)
    print(sorted_list)
    sorted_list = bubble_sort(test_list, desc=True)
    print(sorted_list)