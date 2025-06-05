arr = [8, 4, 7, 3, 1, 5, 6, 2]

def partition(arr, low, high):
    pivot = arr[high]

    i = low -1 # start index for left sublist

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # place pivot in correct position one after end of left sublist

    return i + 1


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quicksort(arr, low, p - 1) # sort left sublist
        quicksort(arr, p + 1, high) # sort right sublist

