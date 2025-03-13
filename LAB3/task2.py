def solve(N, arr):
    # Initialize the minimum value of A[i] to the first element and the max result
    min_value = arr[0]
    max_result = float('-inf')
    
    # Traverse the array starting from the second element (index 1)
    for j in range(1, N):
        # Calculate the value of A[i] + A[j] * 2 with the current min_value
        max_result = max(max_result, min_value + arr[j] * 2)
        
        # Update the min_value for the next iteration
        min_value = min(min_value, arr[j])
    
    return max_result

# Input
N = int(input())
arr = list(map(int, input().split()))

# Calling the function and printing the result
result = solve(N, arr)
print(result)
