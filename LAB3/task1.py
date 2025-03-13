def merge(a, b):
    mrg = []
    i = j = inverse_count = 0
    a_len, b_len = len(a), len(b)

    while i < a_len and j < b_len:
        if b[j] >= a[i] :
            mrg.append(a[i])
            i += 1
        else:
            mrg.append(b[j])
            inverse_count += a_len - i
            j += 1
    
    mrg.extend(b[j:])
    mrg.extend(a[i:])

    return mrg, inverse_count

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    a2, inverse_right = mergeSort(arr[mid:])
    a1, inverse_left = mergeSort(arr[:mid])
    mrg, inverse_shift = merge(a1, a2) 

    inverse_all = inverse_left + inverse_right + inverse_shift
    return mrg, inverse_all


N = int(input())
arr = list(map(int, input().split()))


sorted_arr, inversion_count = mergeSort(arr)


print(inversion_count)
print(*sorted_arr)