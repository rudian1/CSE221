import sys
import bisect

def count_in_range(size, num_queries, data, query_list):
    # Convert array to sorted set (unique values only)
    unique_values = sorted(set(data))
    
    # Dictionary to store prefix sum of element occurrences
    prefix_map = {}
    cumulative_count = 0
    
    for value in unique_values:
        occurrence = data.count(value)  # Count occurrences of value in data
        cumulative_count += occurrence
        prefix_map[value] = cumulative_count  # Store prefix sum
    
    results = []
    for start, end in query_list:
        left_pos = bisect.bisect_left(unique_values, start)
        right_pos = bisect.bisect_right(unique_values, end)
        
        if left_pos == right_pos:
            results.append("0")
        else:
            left_element = unique_values[left_pos]
            right_element = unique_values[right_pos - 1]
            left_prefix = prefix_map[left_element] - data.count(left_element) if left_pos > 0 else 0
            right_prefix = prefix_map[right_element]
            results.append(str(right_prefix - left_prefix))

    sys.stdout.write("\n".join(results) + "\n")

# Read input
size, num_queries = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
query_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_queries)]

# Process and output results
count_in_range(size, num_queries, data, query_list)