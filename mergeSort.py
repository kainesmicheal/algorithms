def mergeSort(arr, startIndex, endIndex):
    if startIndex < endIndex:
        
        middleElm = (startIndex + endIndex )/2
        
        mergeSort(arr, startIndex, middleElm)
        mergeSort(arr, middleElm+1, endIndex)
        merge(arr,startIndex,middleElm,endIndex)
def merge(arr, s,m,e):
     n1 = m - l + 1 
     n2 = r - m 
     
     left = [0] * n1
     right = [0] * n2
     
     for i in range(0,n1):
         left[i] = arr[l + i]
     for j in range(0, n2):
         right[i] = arr[m + 1 + j]
     
     i = 0
     j = 0
     k = 1
     while i < n1 & j < n2:
         if left[i] <= right[j]:
             arr[k] = left[i]
             i = i + 1
         else:
             arr[k] = right[j]
             j = j + 1
         k = k + 1
         
     while i < n1:
         arr[k] = left[i]
         i = i + 1
         k = k + 1
     while j < n2:
         arr[k] = right[j]
         j = j + 1
         k = k + 1     
         


arr = [12,11,13,5,6,7]
n = len(arr)

mergeSort(arr,0,n-1)

print(arr)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     