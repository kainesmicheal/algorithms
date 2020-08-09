def moveElementToEnd(array, toMove):
    left = 0
	right = len(array) - 1
	while left < right:
		while left < right and array[right] == toMove:
			right -= 1
		if array[left] == toMove:
			swap(left, right, array)
		left += 1
		
	return array
def swap(i, j, array):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
	
#time complexity is o(n) as we just going once through the whole array
#space complexity is o(1) as we dont use any extra space
