def findThreeLargestNumbers(array):
    result = [None, None, None]
	for num in array:
		check(result, num)
	return result

def check(result, num):
	if result[2] is None or result[2] < num:
		update(result, num, 2)
	elif result[1] is None or result[1] < num:
		update(result, num, 1)
	elif result[0] is None or result[0] < num:
		update(result, num, 0)

def update(array, num, idx):
	for i in range(idx + 1):
		if i == idx:
			array[i] = num
		else:
			array[i] = array[i + 1]
			
#time complexity is o(n) as we have to traverse all the elements in the array
#space complexity is o(1) as we not storing other than a array of three elements
