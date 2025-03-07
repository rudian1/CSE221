import sys

def two_sum():
    # Read input
    numput1, numput2 = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    l, r = 0, numput1 - 1  # Initialize two pointers

    while l < r:
        cur_sum = arr[l] + arr[r]

        if cur_sum < numput2:
            l += 1  # Increase the left pointer to increase the sum
        elif cur_sum == numput2:
            print(l + 1, r + 1)  # Return the 1-based indices
            return
        else:
            r -= 1  # Decrease the right pointer to decrease the sum

    print(-1)  # If no pair is found, print -1

#call function
two_sum()