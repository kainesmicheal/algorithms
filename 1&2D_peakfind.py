def peak1D():
    array = [2,7,6,5,8,4,5,9]
    length = len(array) - 1
    index_cout = 0
    mid_val = 0
    while(index_cout >= 0):
        if(index_cout == length):
             return array[index_cout]
        mid_val = int((index_cout + length) / 2)
        if( array[mid_val] < array[mid_val + 1] ):
            index_cout = mid_val + 1
        elif(array[mid_val] < array[mid_val - 1]):
            length = mid_val - 1
        else:
            return array[mid_val]
def peak2D(array):
    rows = len(array)
    cols = len(array[0])
    
    j = cols//2 
    row = [i[j] for i in array]
    i = row.index(max(row))
    if j > 0 & array[i][j] < array[i][j-1]:
        return peak2D([row[:j] for row in array])
    elif j < cols - 1 & array[i][j] < array[i][j+1]:
        return peak2D([row[j:] for row in array])
    else:
        return array[i][j]

array = [[2]*5]*5
print(array)
for i in range(2):
    for j in range(2):
        array[i][j] = j + 7;
print(array)

print(peak2D(array))        