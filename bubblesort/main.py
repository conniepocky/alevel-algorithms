l = [1, 6, 7, 3, 9]

def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                print("swapping")
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False

    return arr

print(bubble_sort(l))