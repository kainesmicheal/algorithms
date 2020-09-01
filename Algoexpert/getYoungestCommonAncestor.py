# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = findDepth(descendantOne, topAncestor)
	depthTwo = findDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo:
		return comeUp(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return comeUp(descendantTwo, descendantOne, depthTwo - depthOne)

def comeUp(higherDescendant, lowerDescendant, depth):
	while depth != 0:
		higherDescendant = higherDescendant.ancestor
		depth -= 1
	
	while higherDescendant != lowerDescendant:
		higherDescendant = higherDescendant.ancestor
		lowerDescendant = lowerDescendant.ancestor
	return lowerDescendant
		
	
def findDepth(descendant, topAncestor):
	depth = 0
	currentNode = descendant
	while currentNode != topAncestor:
		currentNode = currentNode.ancestor
		depth += 1
	return depth

#time complexity is o(d) d is the depth of the tree
#space complexity is o(1) constant space
    
