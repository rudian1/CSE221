import bisect

def long_subarray_sum(Num, num2, arr):
    prefix = [0] * (Num + 1)
    for i in range(1, Num + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    
    max_lnt = 0
    for i in range(1, Num + 1):
        target = prefix[i] - num2
        j = bisect.bisect_left(prefix, target)
        if j < i:
            max_lnt = max(max_lnt, i - j)
    
    return max_lnt

# Input handling
Numput1, numput2 = map(int, input().split())
Arr = list(map(int, input().split()))

# Output the result
print(long_subarray_sum(Numput1, numput2, Arr))