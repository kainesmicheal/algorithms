def spiralTraverse(array):
	result = []
	rowStartingIdx, rowEndingIdx = 0, len(array) - 1
	colStartingIdx, colEndingIdx = 0, len(array[0]) - 1
	
	while rowStartingIdx <= rowEndingIdx and colStartingIdx <= colEndingIdx:
		for elm in range(colStartingIdx, colEndingIdx + 1):
			result.append(array[rowStartingIdx][elm])
		for elm in range(rowStartingIdx + 1, rowEndingIdx + 1):
			result.append(array[elm][colEndingIdx])
		for elm in reversed(range(colStartingIdx, colEndingIdx)):
			if rowStartingIdx == rowEndingIdx:
				break
			result.append(array[rowEndingIdx][elm])
		for elm in reversed(range(rowStartingIdx + 1, rowEndingIdx)):
			if colStartingIdx == colEndingIdx:
				break
			result.append(array[elm][colStartingIdx])
			
			
		rowStartingIdx += 1
		rowEndingIdx -= 1
		colStartingIdx += 1
		colEndingIdx -= 1
	return result
#time complexity is o(n * m) as we have row and columns, it can be also written as
#o(N) and the space complexity is o(N) as we n element to be written in a new array


def spiralTraverse(array):
    result = []
	spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
	return result

def spiralFill(array, rowStart, rowEnd, colStart, colEnd, result):
	if rowStart > rowEnd or colStart > colEnd:
		return
	for elm in range(colStart, colEnd + 1):
		result.append(array[rowStart][elm])
		
	for elm in range(rowStart + 1, rowEnd + 1):
		result.append(array[elm][colEnd])
		
	for elm in reversed(range(colStart, colEnd)):
		if rowStart == rowEnd:
			break
		result.append(array[rowEnd][elm])
		
	for elm in reversed(range(rowStart + 1, rowEnd)):
		if colStart == colEnd:
			break
		result.append(array[elm][colStart])
		
	spiralFill(array, rowStart + 1,rowEnd - 1, colStart + 1, colEnd - 1, result)
	return
#time complexity is o(n*m) or 0(N) as the number of rows and cols
#space complexity is 0(n) n is the no of elements in result array
