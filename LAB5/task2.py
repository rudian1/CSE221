import sys
sys.setrecursionlimit(200005)

n, m = map(int, input().split())

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))


if len(u_list) != m or len(v_list) != m:
    print("Edge list size does not match m.")
    sys.exit()

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u = u_list[i]
    v = v_list[i]
    graph[u].append(v)
    graph[v].append(u)

for neighbors in graph:
    neighbors.sort()

visited = [False] * (n + 1)
dfs_order = []
def dfs(u):
    visited[u] = True
    dfs_order.append(u)

    for v in graph[u]:
        if not visited[v]:
            dfs(v)

dfs(1)  

print(" ".join(map(str, dfs_order)))