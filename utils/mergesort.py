from operator import le as less_than_equal_to_operator
from operator import ge as greater_than_equal_to_operator
try:
    from .insertionsort import insertion_sort
except ModuleNotFoundError as e:
    from insertionsort import insertion_sort


def _merge_sorted(sorted_array_1, sorted_array_2, comparison_operator):
    merged_sorted_array = []
    len1 = len(sorted_array_1)
    len2 = len(sorted_array_2)
    i, j = 0, 0
    # print(len1, len2)

    for _ in range(len1 + len2):
        # print("i = {}, j = {}".format(i, j))
        # print(merged_sorted_array)
        if (i < len1) and (j < len2):
            # print('both')
            if comparison_operator(sorted_array_1[i], sorted_array_2[j]):
                merged_sorted_array.append(sorted_array_1[i])
                i += 1
            else:
                merged_sorted_array.append(sorted_array_2[j])
                j += 1
        elif (i < len1) and (j >= len2):
            # print('j finished')
            merged_sorted_array.append(sorted_array_1[i])
            i += 1
        else:
            # print('i finished')
            # (i >= len2) and (j < len2)
            merged_sorted_array.append(sorted_array_2[j])
            j += 1

    return merged_sorted_array


def top_down_split_merge_sort(array, beg, end, comparison_operator):
    """The section of array corresponding to beg:end is considered for sorting
    beg is inclusive and end is exclusive, so array[beg:end] is operative slice."""
    if len(array[beg:end]) <= 1:
        return
    # Effective time reduction optimization: for duo, simply compare and swap
    if len(array[beg:end]) == 2:
        if not comparison_operator(array[beg], array[end - 1]):
            array[beg], array[end - 1] = array[end - 1], array[beg]
            return
        else:
            return

    mid = (beg + end) // 2
    top_down_split_merge_sort(array, beg, mid, comparison_operator)
    top_down_split_merge_sort(array, mid, end, comparison_operator)
    # Effective time reduction optimization: if already sorted, skip merge step
    if comparison_operator(array[mid - 1], array[mid]):
        return
    else:
        sorted_merge = _merge_sorted(array[beg:mid], array[mid:end], comparison_operator)
        array[beg:end] = sorted_merge


def bottom_up_collect_merge_sort(array, comparison_operator):
    array_len = len(array)
    if array_len <= 1:
        return

    def width_gen(cutoff):
        a = 1
        while a < cutoff:
            yield a
            a *= 2

    for width in width_gen(array_len):
        for i in range(0, array_len, 2 * width):
            sec1_beg = i
            sec2_beg = min(i + width, array_len)
            sec2_end = min(i + 2 * width, array_len)
            if sec2_beg == sec2_end:
                continue
            # Effective time reduction optimization: if already sorted, skip merge step
            if comparison_operator(array[sec2_beg - 1], array[sec2_beg]):
                continue
            else:
                sorted_merge = _merge_sorted(array[sec1_beg:sec2_beg], array[sec2_beg:sec2_end], comparison_operator)
                array[sec1_beg:sec2_end] = sorted_merge


def merge_sort(array, approach='top_down', desc=False):
    # Effective time reduction optimization: for small arrays invoke insertionsort
    if len(array) <= 52:
        return insertion_sort(array, desc)

    array = array.copy()
    if desc:
        comparison_operator = greater_than_equal_to_operator
    else:
        comparison_operator = less_than_equal_to_operator
    if approach == 'top_down':
        array_len = len(array)
        top_down_split_merge_sort(array, 0, array_len, comparison_operator)
    elif approach == 'bottom_up':
        bottom_up_collect_merge_sort(array, comparison_operator)
    else:
        raise NotImplementedError('{} type of merge sort not implemented.'.format(approach))
    return array


if __name__ == '__main__':
    # l1, l2 = [1, 3, 6, 7], [2, 4, 5]
    # print(_merge_sorted(l1, l2, less_than_equal_to_operator))
    test_list = [3, 6, 8, 24, 7, 11, 16]
    # top_down_split_merge_sort(test_list, 0, 7, True)
    # bottom_up_collect_merge_sort(test_list, True)
    print(merge_sort(test_list))
    print(merge_sort(test_list, desc=True))
