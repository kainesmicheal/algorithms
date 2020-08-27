def inOrderTraverse(tree, array):
    if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array
	
def postOrderTraverse(tree, array):
    if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array

#time complexity is o(n) as were going through all the nodes
#space complexity is o(n) as were appending those value to a new new array 
#also o(d) as we have d number of frames in call stack due to recursion
	
