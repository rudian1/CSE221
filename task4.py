import sys

def find_first_one(iumput):
    l, r = 0, len(iumput) - 1
    idx = -1  # Default to -1 if no '1' is found

    while l <= r:
        mid = (l + r) // 2
        
        if iumput[mid] == '1':
            idx = mid + 1  # Convert 0-based index to 1-based
            r = mid - 1   # Search in the left half
        else:
            l = mid + 1    # Search in the right half

    return idx

# Read input
Tempu = int(sys.stdin.readline().strip())
results = []

for i in range(Tempu):
    iumput = sys.stdin.readline().strip()
    results.append(str(find_first_one(iumput)))

# Print all results at once (faster output)
sys.stdout.write("\n".join(results) + "\n")