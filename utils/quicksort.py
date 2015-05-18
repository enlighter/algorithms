def quicksort(sort_list, start, end):
	''' sort the list sort_list[start:end] '''

	# debug:
	print("start=%d, end=%d" %(start,end))
	print(sort_list[start:end+1])

	if start == end:
		# debug:
		print("returning without any processing")
		return sort_list

	#Todo: here the choose_pivot method needs to be called
	pivot = sort_list[start]
	# debug:
	print("pivot = %d" %pivot)
	greater_than_pivot_start = start + 1

	for read in range(start+1, end+1):
		if (sort_list[read] < pivot):
			# debug:
			print("%d < %d" %(sort_list[read], pivot))

			if read != greater_than_pivot_start:
				# this condition is imposed to avoid redundant swaps
				sort_list[greater_than_pivot_start], sort_list[read] = sort_list[read], sort_list[greater_than_pivot_start]
				# debug:
				print(sort_list)
			greater_than_pivot_start += 1

	# debug:
	print("after processing: ",sort_list)
	sort_list[start], sort_list[greater_than_pivot_start-1] = sort_list[greater_than_pivot_start-1], sort_list[start]
	# debug:
	print("after correcting pivot position: ",sort_list)

	if greater_than_pivot_start > start:
		sort_list = quicksort(sort_list, start, greater_than_pivot_start-1)
	if greater_than_pivot_start <= end:
		sort_list = quicksort(sort_list, greater_than_pivot_start, end)

	return sort_list

if __name__ == "__main__":
	to_sort = [5,1,3,9,4,7,12,6]
	max_element = len(to_sort) - 1
	sorted = quicksort(to_sort,0,max_element)
	print(sorted)