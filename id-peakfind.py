def peakFind():
    array = [2,3,4,5,6,7,8,9]
    length = len(array) - 1
    index_cout = 0
    mid_val = 0
    while(index_cout >= 0):
        if(index_cout == length):
             return array[index_cout]
        mid_val = int((index_cout + length) / 2)
        
         
             
        if( array[mid_val] <= array[mid_val + 1] ):
            index_cout = mid_val + 1
        elif(array[mid_val] <= array[mid_val - 1]):
            length = mid_val - 1
        else:
            return array[mid_val]


print(peakFind())
            
          