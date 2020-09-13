class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
	#o(n) time | o(1) space
    def buildHeap(self, array):
        parentIdx = ((len(array) - 1) - 1) // 2
		for idx in reversed(range(parentIdx + 1)):
			self.siftDown(idx,len(array)-1,array)	
		return array
	#o(log(n)) time | o(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = (currentIdx * 2) + 1
		while childOneIdx <= endIdx:
			childTwoIdx = (currentIdx * 2) + 2 if (currentIdx * 2) + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childOneIdx] > heap[childTwoIdx]:
				childToSwap = childTwoIdx
			else:
				childToSwap = childOneIdx
			if heap[currentIdx] > heap[childToSwap]:
				self.swap(childToSwap, currentIdx,heap)
				currentIdx = childToSwap
				childOneIdx = (currentIdx * 2) + 1
			else:
				return
		
	#o(log(n)) time | o(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
		while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
			self.swap(currentIdx, parentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx - 1) // 2
		
	#o(1) time
    def peek(self):
        return self.heap[0]
	#o(log(n)) time 
    def remove(self):
		currentIdx = 0
        self.swap(currentIdx,len(self.heap)-1,self.heap)
		value = self.heap.pop()
		self.siftDown(currentIdx,len(self.heap)-1,self.heap)
		return value
	#o(log(n)) time | space o(1)
    def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap)-1,self.heap)
		
	def swap(self,i, j, arr):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
