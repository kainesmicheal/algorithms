class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return helper(tree, float("-inf"), float("inf"))

def helper(tree, minValue, maxValue):
	if tree is None:
		return True
	if tree.value < minValue or tree.value >= maxValue:
		return False
	left = helper(tree.left, minValue, tree.value)
	return left and helper(tree.right, tree.value, maxValue)

#time complexity is o(N) where n is no of nodes
#space complexity is o(d) where d is the depth of the tree
