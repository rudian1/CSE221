import heapq

def dijkstra(N, adj_list, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)] 

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

N, M, S, T = map(int, input().split())

adj_list = []
for i in range(N + 1):
    adj_list.append([])

for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

distAlice = dijkstra(N, adj_list, S)
distBob = dijkstra(N, adj_list, T)

min_time = float('inf')
best_node = -1

for node in range(1, N + 1):
    if distAlice[node] != float('inf') and distBob[node] != float('inf'):
        meet_time = max(distAlice[node], distBob[node])
        if meet_time < min_time:
            min_time = meet_time
            best_node = node
        elif meet_time == min_time:
            best_node = min(best_node, node)

if best_node == -1:
    print(-1)
else:
    print(min_time, best_node)
