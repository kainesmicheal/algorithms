def heapify(A):
    n = len(A) - 1 
    for node in range(n//2,-1,-1):
        siftDown(A,node)
    return

def pushHeap(A,val):
    A.append(val)
    
    siftUp(A,len(A) - 1)
    
    return

def popHeap(A):
    n = len(A) - 1
    
    swap(A,0,n)
    
    maxVal = A.pop(n)
    
    siftDown(A,0)
    
    return maxVal

def swap(A,i,j):
    A[i],A[j] = A[j], A[i]
    
    return

def siftDown(A, node):
    child = 2 * node + 1 
    
    if child > len(A) - 1:
        return
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    if A[node] < A[child]:
        swap(A,node,child)
        siftDown(A, child)
    else:
        return
    
def siftUp(A,node):
    parent = (node - 1) // 2
    if A[parent] < A[node]:
        swap(A,node,parent)
    if parent <= 0:
        return
    else:
        siftUp(A,parent)
        
arr = [1,2,3,4,5,6,7]

maxx = []
while (len(arr) > 0):
    heapify(arr)
    maxVal = popHeap(arr)
    maxx.append(maxVal)
    
print(maxx)