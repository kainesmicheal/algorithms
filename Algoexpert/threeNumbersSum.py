def threeNumberSum(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return triplets

#time complexity is 0(n^2) as we are iterating through the array several times
#space complexity is 0(n) as we have to store the triplets
