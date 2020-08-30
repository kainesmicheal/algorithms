def levenshteinDistance(str1, str2):
    nums = [[x for x in range(len(str1)+1)] for y in range(len(str2) + 1)]
	for i in range(1, len(str2) + 1):
		nums[i][0] = i
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				nums[i][j] = nums[i - 1][j - 1]
			else:
				nums[i][j] = 1 + min(nums[i][j-1], nums[i-1][j-1], nums[i-1][j])
	return nums[-1][-1]

#time complexity is o(nm) as we two arrays of size n and m
#space complexity is o(nm) as we create an array of size nm


def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
	big = str1 if len(str1) >= len(str2) else str2
	evenEdits = [x for x in range(len(small) + 1)]
	oddEdits = [None for x in range(len(small) + 1)]
	for i in range(1, len(big) + 1):
		if i % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits
		currentEdits[0] = i
		for j in range(1,len(small) + 1):
			if big[i-1] == small[j-1]:
				currentEdits[j] = previousEdits[j - 1]
			else:
				currentEdits[j] = 1 + min(currentEdits[j - 1], previousEdits[j], previousEdits[j - 1])
	return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

#time complexity is o(n * m) n and m are the size of size
#space complexity is o(min(n,m)) as we are using only two array of n or m in a iteration
