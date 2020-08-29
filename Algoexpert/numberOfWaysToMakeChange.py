def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
	ways[0] = 1
	for coin in denoms:
		for amount in range(1, n + 1):
			if coin <= amount:
				ways[amount] += ways[amount - coin]
	return ways[n]
			
#time complexity is o(nd) as we have n number of amount and d no of coins
#space complexity is o(n) as we create a new array of size n
