#read inputs
line1 = input().split()
n,m,s,d,k = int(line1[0]), int(line1[1]),int(line1[2]),int(line1[3]),int(line1[4])
#build graph
graph = []
for i in range(n + 1):
    graph.append([])
for i in range(m):
    edge = input().split()
    u = int(edge[0])
    v = int(edge[1])
    graph[u].append(v)
# ---- BFS from s to k ----
dist_s = []
parent_s = []
for i in range(n + 1):
    dist_s.append(-1)
    parent_s.append(-1)
queue = []
dist_s[s] = 0
queue.append(s)

while len(queue) > 0:
    u = queue[0]
    del queue[0]
    for i in range(len(graph[u])):
        v = graph[u][i]
        if dist_s[v] == -1:
            dist_s[v] = dist_s[u] + 1
            parent_s[v] = u
            queue.append(v)
# ---- BFS from k to d ----
dist_k = []
parent_k = []
for i in range(n + 1):
    dist_k.append(-1)
    parent_k.append(-1)
queue = []
dist_k[k] = 0
queue.append(k)
while len(queue) > 0:
    u = queue[0]
    del queue[0]
    for i in range(len(graph[u])):
        v = graph[u][i]
        if dist_k[v] == -1:
            dist_k[v] = dist_k[u] + 1
            parent_k[v] = u
            queue.append(v)
# ---- Check if path exists ----
if dist_s[k] == -1 or dist_k[d] == -1:
    print(-1)
else:
    # Path from s to k
    path_s_k = []
    cur = k
    while cur != -1:
        path_s_k.append(cur)
        cur = parent_s[cur]
    path_s_k.reverse()
    # Path from k to d (excluding k)
    path_k_d = []
    cur = d
    while cur != k:
        path_k_d.append(cur)
        cur = parent_k[cur]
    path_k_d.reverse()
    # Combine paths
    full_path = []
    for i in range(len(path_s_k)):
        full_path.append(path_s_k[i])
    for i in range(len(path_k_d)):
        full_path.append(path_k_d[i])
    print(len(full_path) - 1)
    for i in range(len(full_path)):
        print(full_path[i], end=" ")