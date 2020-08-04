# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depth = 0):
    if root == None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

#in this case the time complexity is o(n) as we are traversing through every node
#the space compexity is o(h) where, h is the height of the tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
	totalDepth = 0
	stack = [{"node" : root, "depth": 0}]
	while len(stack) != 0:
		currentNode = stack.pop()
		node = currentNode["node"]
		depth = currentNode["depth"]
		if node == None:
			continue
		totalDepth += depth
		stack.append({"node" : node.left, "depth": depth + 1})
		stack.append({"node" : node.right, "depth": depth + 1})
	return totalDepth

#in this case the time compexity is o(n) as we got to traverse every node of the 
#tree and space complexity in average case is 0(log(n)) as we could potentially 
#elimiate half of the branch in a given point and o(n) in the worst case

