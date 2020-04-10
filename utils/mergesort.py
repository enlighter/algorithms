def top_down_merge_sorted(sorted_array_1, sorted_array_2, desc=False):
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
            if not desc:
                if sorted_array_1[i] <= sorted_array_2[j]:
                    merged_sorted_array.append(sorted_array_1[i])
                    i += 1
                else:
                    merged_sorted_array.append(sorted_array_2[j])
                    j += 1
            else:
                if sorted_array_1[i] >= sorted_array_2[j]:
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


def top_down_split_merge_sort(array, beg, end, desc=False):
    """The section of array corresponding to beg:end is considered for sorting
    beg is inclusive and end is exclusive, so array[beg:end] is operative slice."""
    if len(array[beg:end]) <= 1:
        return

    mid = (beg + end) // 2
    top_down_split_merge_sort(array, beg, mid, desc)
    top_down_split_merge_sort(array, mid, end, desc)
    sorted_merge = top_down_merge_sorted(array[beg:mid], array[mid:end], desc)
    array[beg:end] = sorted_merge


if __name__ == '__main__':
    l1, l2 = [1, 3, 6, 7], [2, 4, 5]
    print(top_down_merge_sorted(l1, l2))
    test_list = [3, 6, 8, 24, 7, 11, 16]
    top_down_split_merge_sort(test_list, 0, 7, True)
    print(test_list)
