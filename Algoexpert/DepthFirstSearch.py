class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array
	
	#in this case the time complexity is o(v + e) that is no of vertices and no of 
	#edges and space compexity in worst case is o(v)
