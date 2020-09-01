def riverSizes(matrix):
    sizes = []
	visited = [[False for value in row] for row in matrix]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if visited[i][j]:
				continue
			traverse(i, j, matrix, visited, sizes)
	return sizes

def traverse(i, j, matrix, visited, sizes):
	currentRiverSize = 0
	nodesToVisit = [[i,j]]
	while len(nodesToVisit) > 0:
		currentNode = nodesToVisit.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		currentRiverSize += 1
		neighours = getNeighours(i, j, visited, matrix)
		for val in neighours:
			nodesToVisit.append(val)
	if currentRiverSize > 0:
		sizes.append(currentRiverSize)

def getNeighours(i, j, visited, matrix):
	arrayOfNeighours = []
	if i > 0 and visited[i - 1][j] == False:
		arrayOfNeighours.append([i - 1,j])
	if i < len(matrix) - 1 and visited[i + 1][j] == False:
		arrayOfNeighours.append([i + 1,j])
	if j > 0 and visited[i][j - 1] == False:
		arrayOfNeighours.append([i,j - 1])
	if j < len(matrix[0]) - 1 and visited[i][j + 1] == False:
		arrayOfNeighours.append([i,j+1])
	return arrayOfNeighours

#time complexity is o(w.h) wight and height of the matrix
#space complexity is 0(w.h) the size of the new matrix we use 
