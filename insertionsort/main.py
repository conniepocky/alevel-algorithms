l = [3, 9, 7, 5, 2]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]

        j = i-1 # beginning of sorted part

        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr

print(insertion_sort(l))