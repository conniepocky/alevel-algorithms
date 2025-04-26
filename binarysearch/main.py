list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(list, value):
    if not list:
        print("NOT found")
        return False
    
    mid = len(list) // 2
    
    if list[mid] == value:
        print("found at index ", mid)
        return True
    elif value > list[mid]:
        return binary_search(list[mid+1:], value)
    else:
        return binary_search(list[:mid], value)

print(binary_search(list, 3))