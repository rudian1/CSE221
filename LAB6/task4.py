import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, R = map(int, input[ptr:ptr+2])
    ptr += 2
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input[ptr:ptr+2])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [0] * (N + 1)
    children = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    q = deque([R])
    visited[R] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                q.append(v)
    
    size = [1] * (N + 1)
    stack = [(R, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            for child in children[node]:
                size[node] += size[child]
        else:
            stack.append((node, True))
            for child in reversed(children[node]):
                stack.append((child, False))
    
    Q = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(Q):
        X = int(input[ptr])
        ptr += 1
        output.append(str(size[X]))
    print('\n'.join(output))



if __name__ == "__main__":
    main()