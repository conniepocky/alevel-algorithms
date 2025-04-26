l = [1, 4, 3, 9, 7, 2]

def merge(left, right):
    print("left", left)
    print("right", right)
    final = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1

    if i < len(left):
        final.extend(left[i:])
    if j < len(right):
        final.extend(right[j:])

    return final

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    print("left_half", left_half)
    print("right_half", right_half)

    return merge(left_half, right_half)

print(merge_sort(l))