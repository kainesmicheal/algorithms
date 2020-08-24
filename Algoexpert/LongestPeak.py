def longestPeak(array):
	longestPeakLen = 0
	i = 1
	while i < len(array) - 1:
		isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
		if not isPeak:
			i += 1
			continue
		
		leftIdx = i - 1
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		rightIdx = i + 1
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
		
		currentPeakLen = rightIdx - leftIdx - 1
		longestPeakLen = max(currentPeakLen, longestPeakLen)
		
		i = rightIdx
		
	return longestPeakLen

#time complexity is o(N) as  we just iterating through all the elments once and the 
#one side of the peak and space complexity is o(1) as we are not using any other space
