n,m = input().split()
n = int(n)
m = int(m)
graph = []
for i in range(n + 1):
    graph.append([])  # index 0 is unused
for i in range(m):
    u, v = input().split()
    u = int(u)
    v = int(v)
    graph[u].append(v)
    graph[v].append(u)
visited = []
for i in range(n + 1):
    visited.append(False)
queue = []
bfs_order = []
# Start BFS from node 1
visited[1] = True
queue.append(1)
while len(queue) > 0:
    u = queue[0]
    del queue[0]  # pop from front
    bfs_order.append(u)
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = True
            queue.append(v)
# Print the BFS order
for node in bfs_order:
    print(node, end=" ")