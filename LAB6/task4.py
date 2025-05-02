import sys
sys.setrecursionlimit(1 << 25)

dta = sys.stdin.read().split()
idx = 0
N = int(dta[idx])
idx += 1
R = int(dta[idx])
idx += 1
adj = []
for i in range(N + 1):
    adj.append([])
for edge in range(N - 1):
    u = int(dta[idx])
    idx += 1
    v = int(dta[idx])
    idx += 1
    adj[u].append(v)
    adj[v].append(u)

prnt = [0] * (N + 1)
size = [0] * (N + 1)
stack = []
stack.append((R, None, False))
while stack:
    node, par, processed = stack.pop()
    if not processed:
        prnt[node] = par
        stack.append((node, par, True))
        
        for neighbor in reversed(adj[node]):
            if neighbor != par:
                stack.append((neighbor, node, False))
    else:
        size[node] = 1
        for neighbor in adj[node]:
            if neighbor != par:
                size[node] += size[neighbor]


Q = int(dta[idx])
idx += 1

for query in range(Q):
    X = int(dta[idx])
    idx += 1
    print(size[X])