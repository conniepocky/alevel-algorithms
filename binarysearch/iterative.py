list = [1,2,3,4,5,6,7]

def binary_search(arr, value):
    i = 0
    j = len(arr)-1
    
    while j >= i:
        mid = (j+i) // 2
        print(mid, i, j)
        
        if arr[mid] == value:
            return value
        elif arr[mid] > value:
            j = mid-1
        else:
            i = mid+1
          
    return
            
print(binary_search(list, 7))