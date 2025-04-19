from collections import deque

n_m_s_d = input().split()
n,m,s,d = int(n_m_s_d[0]), int(n_m_s_d[1]),int(n_m_s_d[2]), int(n_m_s_d[3])


# Read the u and v edge lists
list_u = list(map(int, input().split()))
list_v = list(map(int, input().split()))


# Create adjacency list
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u = list_u[i]
    v = list_v[i]
    graph[u].append(v)
    graph[v].append(u)
    

# Sort neighbors for lexicographical order
for i in range(n + 1):
    graph[i].sort()

# Initialize BFS variables
visit = [False] * (n + 1)
reach = [-1] * (n + 1)
parent = [-1] * (n + 1)

que = deque()
visit[s] = True
reach[s] = 0
que.append(s)


# BFS loop
while que:
    u = que.popleft()
    for v in graph[u]:
        if not visit[v]:
            visit[v] = True
            reach[v] = reach[u] + 1
            parent[v] = u
            que.append(v)


# If destination not reachable
if not visit[d]:
    print(-1)
else:
    # Reconstruct the path
    path = []
    current = d
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    # Print the result
    print(len(path) - 1)
    print(" ".join(map(str, path)))
