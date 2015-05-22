def quicksort_(sort_list, start, end):
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

	greater_than_pivot_start -= 1
	if greater_than_pivot_start > start:
		sort_list = quicksort_(sort_list, start, greater_than_pivot_start-1)
	if greater_than_pivot_start < end:
		sort_list = quicksort_(sort_list, greater_than_pivot_start+1, end)

	return sort_list

def _choose_pivot_(sort_list, start, end):
	''' method to choose an pivot for efficient
	quicksort implementation '''

class quicksort(object):
	'''
	This quicksort class sorts the
	entire list 'to_sort', if you want
	to sort a part of the list then pass
	list[start:end+1] as the parameter
	list to be sorted
	'''
	def __init__(self, to_sort):
		self.sorted = to_sort
		self.last_pos = len(self.sorted) - 1
		if self.last_pos > 0:
			self._process_(0, self.last_pos)

	def _process_(self, beg, end):
		pass

	def _partition_(self, beg, end):
		pivot = self.sorted[beg]
		# debug:
		print("pivot = %d" %pivot)
		greater_than_pivot_start = beg + 1

		for read in range(beg+1, end+1):
			if (self.sorted[read] < pivot):
				# debug:
				print("%d < %d" %(self.sorted[read], pivot))

				if read != greater_than_pivot_start:
					# this condition is imposed to avoid redundant swaps
					self.sorted[greater_than_pivot_start], self.sorted[read] = self.sorted[read], self.sorted[greater_than_pivot_start]
					# debug:
					print(self.sorted)
				greater_than_pivot_start += 1

		# debug:
		print("after processing: ",self.sorted)
		self.sorted[beg], self.sorted[greater_than_pivot_start-1] = self.sorted[greater_than_pivot_start-1], self.sorted[beg]
		# debug:
		print("after correcting pivot position: ",self.sorted)

		return greater_than_pivot_start-1

if __name__ == "__main__":
	to_sort = [5,1,3,9,4,7,12,6]
	max_element = len(to_sort) - 1
	sorted = quicksort_(to_sort,0,max_element)
	print(sorted)