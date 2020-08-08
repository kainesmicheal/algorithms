def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	leftIdx = 0
	rightIdx = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while leftIdx < len(arrayOne) and rightIdx < len(arrayTwo):
		leftVal = arrayOne[leftIdx]
		rightVal = arrayTwo[rightIdx]
		current = abs(leftVal - rightVal)
		if leftVal < rightVal:
			leftIdx += 1
		elif rightVal < leftVal:
			rightIdx += 1
		else:
			return [leftVal, rightVal]
		if current < smallest:
			smallest = current
			smallestPair = [leftVal, rightVal]
	return smallestPair

#time compexity is o(nlog(n)) which is for the sorting algorithm used and the while 
#just used o(n) so it wont be taken in the over all time
#space complexity is o(1) as there is no extra space used
