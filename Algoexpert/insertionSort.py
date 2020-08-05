def insertionSort(array):
    for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			swap(j, j-1, array)
			j -= 1
	return array

def swap(i, j, array):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	
#the time complexity is o(n^2) as we got to iterate through the array serveral times
#space complexity is o(1) as there is just in place swaps
