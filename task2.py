import sys

def max_sum():
    numput1 = int(sys.stdin.readline().strip())
    total_number = sys.stdin.readline().strip().split()
    numbers = []
    
    for num_str in total_number:
        numbers.append(int(num_str))
    mx_val = float('-inf')
    mx_pre = numbers[0]
    
    for j in range(1, numput1):
        mx_val = max(mx_val, mx_pre + numbers[j] ** 2)
        mx_pre = max(mx_pre, numbers[j])
    sys.stdout.write(str(mx_val) + "\n")

max_sum()
