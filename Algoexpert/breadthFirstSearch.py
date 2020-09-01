class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.name)
			if len(current.children) == 0:
				continue
			else:
				for child in current.children:
					queue.append(child)
		return array

	#time complexity is o(v + e) as we have v num of vertices and edges 
	#space complexity is o(v) as we have v num of vertices to store in a array
			
