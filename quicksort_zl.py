#implement a quick sort in python
#it can sort in O(nlogn) on average (for most cases), worse case O(n^2) if the pivot chosen is either the highest or lowest value


import random
test = random.sample(range(0, 30), 15)


def quicksort(list_to_sort, low_index, high_index):
	if((high_index - low_index) > 0):	#continue with the algorithm
		p = partition(list_to_sort, low_index, high_index)
		#once the partition is complete
		quicksort(list_to_sort, low_index, p-1) #high index would be p-1
		quicksort(list_to_sort, p+1, high_index)

#major chunk of the work
def partition(list_to_sort, low_index, high_index):
	divider = low_index
	pivot = high_index #it could be any element, but using high index is convinient
	
	for i in range(low_index, high_index):
		#compare pivot to each individual element
		if (list_to_sort[i] < list_to_sort[pivot]):
			#swap those two
			list_to_sort[i], list_to_sort[divider] = list_to_sort[divider], list_to_sort[i]
			divider += 1
	#once it sorts from low index to high index
	list_to_sort[pivot], list_to_sort[divider] = list_to_sort[divider], list_to_sort[pivot]
	return divider
print("The test sample is: ", test)
quicksort (test, 0, len(test) -1)
print("After the quicksort: ",test)