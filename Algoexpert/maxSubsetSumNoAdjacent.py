def maxSubsetSumNoAdjacent(array):
    if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	first = max(array[0], array[1])
	second = array[0]
	for i in range(2, len(array)):
		current = max(first,second + array[i])
		second = first
		first = current
	return first

#time complexity is o(n) as we have n numbers in array
#space complexity is o(1) as we just constant time operations


def maxSubsetSumNoAdjacent(array):
    if not len(array):
		return 0
	elif len(array) == 1:
		return array[0]
	maxSums = array[:]
	maxSums[1] = max(array[0], array[1])
	for i in range(2, len(array)):
		maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
	return maxSums[-1]

#time complexity is o(n) as we have n numbers to go through
#space complexity is o(n) as we create a new array of lenght n
