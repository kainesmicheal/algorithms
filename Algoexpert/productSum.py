def productSum(array, multiplier = 1):
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier + 1)
		else:
			sum += element
	return sum * multiplier

#time compexity is o(n) where n is no. of total element in everry array 
#space compexity is 0(d) where d is the depeth of the array that is no. of inner array
