def binarySearch(array, target):
    return helper(array, target, 0, len(array) - 1)

def helper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	potentialVal = array[middle]
	if potentialVal == target:
		return middle
	elif potentialVal < target:
		return helper(array, target, middle + 1, right)
	elif potentialVal > target:
		return helper(array, target, left, middle - 1)
	
#time compexity is o(log(n)) as we are eliminating help of the elements in every
#search and space compexity is o(log(n)) as there will be log(n) frames in call stack



def binarySearch(array, target):
    left, right = 0, len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		potentialVal = array[middle]
		if potentialVal == target:
			return middle
		elif potentialVal < target:
			left = middle + 1
		else:
			right = middle - 1
	return -1

#time complexity is o(log(n)) as we are elemination half of the array 
#space complexity is o(1) as we are not using any extra space
