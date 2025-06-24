list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(low, high, list, value):
    if low > high:
        print("NOT found")
        return False

    mid = (low + high) // 2

    if list[mid] == value:
        print("found at index ", mid)
        return True
    elif value > list[mid]:
        return binary_search(mid + 1, high, list, value)
    else:
        return binary_search(low, mid - 1, list, value)

print(binary_search(0, len(list) - 1, list, 3))