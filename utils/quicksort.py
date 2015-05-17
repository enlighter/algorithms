def quicksort(sort_list, start, end):
	''' sort the list sort_list[start:end] '''

	if start == end:
		return sort_list

	#Todo: here the choose_pivot method needs to be called
	pivot = sort_list[start]
	greater_than_pivot_start = start + 1

	for read in range(start+1, end):
		if sort_list[read] < pivot:
			sort_list[greater_than_pivot_start], sort_list[read] = sort_list[read], sort_list[greater_than_pivot_start]
			print(sort_list)
			greater_than_pivot_start += 1

	sort_list[start], sort_list[greater_than_pivot_start-1] = sort_list[greater_than_pivot_start-1], sort_list[start]

	if greater_than_pivot_start > start:
		sort_list = quicksort(sort_list, start, greater_than_pivot_start-1)
	if greater_than_pivot_start < end:
		sort_list = quicksort(sort_list, greater_than_pivot_start+1, end)

	return sort_list

if __name__ == "__main__":
	to_sort = [5,1,3,9,4,7,12,6]
	max_element = len(to_sort)
	sorted = quicksort(to_sort,0,max_element)
	print(sorted)