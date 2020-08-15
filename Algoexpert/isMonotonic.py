def isMonotonic(array):
	if len(array) <= 2:
		return True
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if breaksDirection(direction, array[i - 1], array[i]):
			return False		
	return True

def breaksDirection(direction, previous, current):
	difference = current - previous
	if direction > 0:
		return difference < 0
	return difference > 0

#time complexity is o(n) as we iteration through the whole array once
#space complexity is o(1) as we not using any extra space

def isMonotonic(array):
    isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			isNonIncreasing = False
		if array[i] < array[i - 1]:
			isNonDecreasing = False 
	return isNonDecreasing or isNonIncreasing

#time complexity is o(n) as we iterating through the whole array once
#space complexity is 0(1) as we are not using any extra space
