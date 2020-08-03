def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i+1, len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

#in this case time complexity is o(n^2)
#and space complexity is 0(1)
		
def twoNumberSum(array, targetSum):
    nums = {}
	for num in array:
		potentialVal = targetSum - num
		if potentialVal in nums:
			return [potentialVal, num]
		else:
			nums[num] = True
	return []
#in this case the time complexity is o(n)
#space complexity is o(n)

def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		potentialVal = array[left] + array[right]
		if potentialVal == targetSum:
			return [array[left], array[right]]
		elif potentialVal < targetSum:
			left += 1
		elif potentialVal > targetSum:
			right -= 1
	return []
#in this case the time complexity is 0(n log(n))
#space compexity is n(1)
