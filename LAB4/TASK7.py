import math
import sys
input = sys.stdin.read
print = sys.stdout.write

def solve():
    Numput1 = input().splitlines()
    n, q = map(int, Numput1[0].split())
    
    adjcnt = [[] for _ in range(n+1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and math.gcd(i, j) == 1:
                adjcnt[i].append(j)
    
    for i in range(1, n + 1):
        adjcnt[i].sort()
    

    res = []
    for line in Numput1[1 + n:]:
        X, K = map(int, line.split())
        if K <= len(adjcnt[X]):
            res.append(str(adjcnt[X][K-1]))
        else:
            res.append("-1")
    

    print("\n".join(res) + "\n")

solve()
