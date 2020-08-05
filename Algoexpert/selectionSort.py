def selectionSort(array):
    currentIdx = 0
	while currentIdx < len(array) - 1:
		smallestIdx = currentIdx
		for i in range(currentIdx + 1, len(array)):
			if array[i] < array[smallestIdx]:
				smallestIdx = i
		swap(currentIdx, smallestIdx, array)
		currentIdx += 1
	return array

def swap(i, j, array):
	temp = array[i] 
	array[i] = array[j]
	array[j] = temp

#space complexity is o(1) as only the values are changed
#time complexity is o(n^2) as we will be iterating the array n*n times
