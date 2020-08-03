def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx != len(array) and seqIdx != len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)

#in this case the time compexity is o(n) as we will only have to traverse through
#lenght of the sequence list in the worst case and space complexity is o(1)


def isValidSubsequence(array, sequence):
    seqIdx = 0
	for val in array:
		if seqIdx == len(sequence):
			break
		if val == sequence[seqIdx]:
			seqIdx += 1
	return seqIdx == len(sequence)

#time complexity is o(n) as it just traverse n elements in wrost case
#space compelexity is o(1)
