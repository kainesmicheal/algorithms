def mergeSort(arr, startIndex, endIndex):
    if endIndex - startIndex > 1:
        middleElm = (startIndex + endIndex )//2
        mergeSort(arr, startIndex, middleElm)
        mergeSort(arr, middleElm, endIndex)
        merge(arr,startIndex,middleElm,endIndex)
        

def merge(arr, s,m,e):
     left = arr[s:m]
     right = arr[m:e]
     k = s 
     i = 0
     j = 0
     while (s + i < m and m + j < e):
        if(left[i] <= right[j]):
             arr[k] = left[i]
             i = i + 1
        else:
             arr[k] = right[j]
             j =j + 1 
        k = k + 1 
     if s + i < m:
         while k < e:
             arr[k] = left[i]
             i = i + 1 
             k = k + 1
         while k < e:
             arr[k] = right[j]
             j = j + 1 
             k = K + 1
arr = [12,14,11,5,8,6]
n = len(arr)
mergeSort(arr, 0, n)
print(arr)
     
     
     
     