# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    return helper(tree, target, tree.value)

def helper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
	return closest

#in this case the time complexity is 0(log (n)) and space compexity is o(1)



# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
	return helper(tree, target, tree.value)

def helper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - tree.value) < abs(target - closest):
		closest = tree.value
	if tree.value < target:
		return helper(tree.right, target, closest)
	elif tree.value > target:
		return helper(tree.left, target, closest)
	else:
		return closest
	
#time compexity is o (log (n)) as it is bst and in average case we could eliminate 
#one side of the tree, but in worst case the time compexity would be o(n) as we have
#to look at every node of the tree
#space compexity is o (log(n)) as the recursion create a stack for every time the 
#helper is called




