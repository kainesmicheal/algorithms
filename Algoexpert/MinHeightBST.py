class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightBst(array):
    return helper(array, 0, len(array) - 1)

def helper(array, startIdx, endIdx):
	if startIdx > endIdx:
		return None
	midIdx = (startIdx + endIdx) // 2
	value = array[midIdx]
	bst = BST(value)
	bst.left = helper(array, startIdx, midIdx - 1)
	bst.right = helper(array, midIdx + 1, endIdx)
	return bst

#time complexity is o(n) as we are not using the insertion method of ths bst class
#space complexity is o(n) as n number of nodes

def minHeightBst(array):
	return helper(array, None, 0, len(array) - 1)

def helper(array, bst, startIdx, endIdx):
	if startIdx > endIdx:
		return 
	midIdx = (startIdx + endIdx) // 2
	value = array[midIdx]
	if bst is None:
		bst = BST(value)
	else:
		if value < bst.value:
			bst.left = BST(value)
			bst = bst.left
		else:
			bst.right = BST(value)
			bst = bst.right
	helper(array, bst, startIdx, midIdx - 1)
	helper(array, bst, midIdx + 1, endIdx)
	return bst

#time complexity is o(n) as we are not using the insertion method of the bst class
#space complexity is o(n) as we have n nodes

def minHeightBst(array):
	return helper(array, None, 0, len(array) - 1)

def helper(array, bst, startIdx, endIdx):
	if startIdx > endIdx:
		return 
	midIdx = (startIdx + endIdx) // 2
	value = array[midIdx]
	if bst is None:
		bst = BST(value)
	else:
		bst.insert(value)
	helper(array, bst, startIdx, midIdx - 1)
	helper(array, bst, midIdx + 1, endIdx)
	return bst

#time complexity is o(nlog(n)) as we have n no of node call and the inseration call
#takes o(log(n)) this o(nlog(n))
#space complexity is o(n) as n number of nodes
