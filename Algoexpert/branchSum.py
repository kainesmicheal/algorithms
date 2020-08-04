# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums = []
	helper(root, 0, sums)
	return sums

def helper(node, runningSum, resultArray):
	if node == None:
		return
	runningSum = node.value + runningSum
	if node.left == None and node.right == None:
		resultArray.append(runningSum)
		return
	helper(node.left, runningSum, resultArray)
	helper(node.right, runningSum, resultArray)

#in this clase the time compexity is 0(n) as we should traverse every node of the
#tree and the space compexity is o(log(n)) in average as we would only be having
#maxing function in out stack equal to the height of the tree, in worst case,
#when the treee has only one branch with linked list kind structure, the 
#space would be o(n)
