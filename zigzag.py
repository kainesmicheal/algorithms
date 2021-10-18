def zigzagTraverse(array):
	visited = []
	result = []
	i = 0
	j = 0
	while len(result) < len(array)*len(array[0]):
		if getString(i,j) in visited and i - 1< 0 :
			if j == len(array[0])-1:
				if i+1 <= len(array) - 1:
					i += 1
			else:
				if j+1 <= len(array[0]) - 1:
					j += 1
		elif getString(i,j) in visited and j - 1 < 0:
			if i == len(array) -1:
				j += 1
			else:
				if i+1 <= len(array) - 1:
					i += 1
		elif getString(i,j) in visited and getString(i-1,j+1) in visited:
			j += 1	
		elif getString(i,j) in visited and getString(i+1,j-1) in visited:
			if i+1 <= len(array) - 1:
				i += 1
		if i <= len(array) - 1:
			result.append(array[i][j])
			visited.append(getString(i,j))
		
		
		if i == 0 and j == 0:
			i +=1
		else:
			if i - 1 >= 0 and j + 1 < len(array[0]):
				if getString(i-1,j+1) not in visited:
					i -= 1
					j += 1	
			if j - 1 >= 0 and i + 1 < len(array):
				if getString(i+1,j-1) not in visited:
					j -= 1
					i += 1
			
	return result

def getString(i,j):
	return str(i) + " , " + str(j)
