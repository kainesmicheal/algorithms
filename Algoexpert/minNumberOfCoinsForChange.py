def minNumberOfCoinsForChange(n, denoms):
    nums = [float("inf") for i in range(n + 1)]
	nums[0] = 0
	for denom in denoms:
		for amount in range(len(nums)):
			if denom <= amount:
				nums[amount] = min(nums[amount], nums[amount - denom] + 1)
	return nums[n] if nums[n] != float("inf") else -1

#time complexity is o(nd) as we have two array of size n and d
#space complexity is o(n) as we create a array of size n+1
