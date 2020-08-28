class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def swap(tree):
	temp = tree.left
	tree.left = tree.right
	tree.right = temp
        
def invertBinaryTree(tree):
    if tree is None:
		return 
	swap(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

#time complexity is o(n) as we have n nodes
#space complexity is o(d) as will have d nodes in call stack at a point

def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		currentNode = queue.pop(0)
		if currentNode is None:
			continue
		swap(currentNode)
		queue.append(currentNode.left)
		queue.append(currentNode.right)

#time complexity is o(n) as we got to through all nodes
#space complexity is o(n) as there will be n number of nodes in queue at a point
