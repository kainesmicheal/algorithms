def hasSingleCycle(array):
    numOfElemsVisited = 0
	currentIdx = 0
	while numOfElemsVisited < len(array):
		if numOfElemsVisited != 0 and currentIdx == 0:
			return False
		currentIdx = jump(currentIdx, array)
		numOfElemsVisited += 1
	return currentIdx == 0

def jump(currentIdx, array):
	currentIdx = (currentIdx + array[currentIdx]) % len(array)
	return currentIdx if currentIdx >= 0 else currentIdx + len(array)

#time complexity is o(n) as we go through all elements once
#space complexity is o(1)
