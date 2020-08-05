def bubbleSort(array):
	isSorted = False
	counter = 0
	while not isSorted:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array [i + 1]:
				swap(i, i + 1, array)
				isSorted = False
		counter += 1
	return array

def swap(i, j, array):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

#the time complexity is o(n^2) as we will iterate through the array serveral times
#the space complexit is o(1) as we are just doing in place swaps 
