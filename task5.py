import sys
import bisect

def count_numbers(numput, qumput, ARR, q):
    results = []
    for i, j in q:
        left_idx = bisect.bisect_left(ARR, i)
        right_idx = bisect.bisect_right(ARR, j)
        results.append(str(right_idx - left_idx))
    
    # Print all results at once for efficiency
    sys.stdout.write("\n".join(results) + "\n")

# Read input
numput, qumput = map(int, sys.stdin.readline().split())
ARR = list(map(int, sys.stdin.readline().split()))
q = [tuple(map(int, sys.stdin.readline().split())) for i in range(qumput)]

# Process and output results
count_numbers(numput, qumput, ARR, q)
