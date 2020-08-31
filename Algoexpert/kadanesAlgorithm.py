def kadanesAlgorithm(array):
	currentSum = array[0]
	largestSum = array[0]
	for num in array[1:]:
		currentSum = max(currentSum + num, num)
		largestSum = max(currentSum, largestSum)
	return largestSum

#time complexity is o(n) as we have to iterate through the array of n elements
#space complexity is o(1)
