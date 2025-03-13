import sys

def collect_elm(arr, l, r, result):
    if l > r:
        return
    middle = (l + r) // 2
    result.append(arr[middle])
    collect_elm(arr, l, middle - 1, result)  
    collect_elm(arr, middle + 1, r, result)


numput = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

res = []
collect_elm(arr, 0, numput - 1, res)

output = ' '.join(map(str, res))
sys.stdout.write(output + '\n')