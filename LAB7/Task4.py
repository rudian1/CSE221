import heapq

N, M, S, D = map(int, input().split())
weights = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)


inf = 1 << 60
min_cost = [inf] * (N + 1)
min_cost[S] = weights[S - 1]

heap = [(weights[S - 1], S)] 

while heap:
    cost_u, u = heapq.heappop(heap)

    if u == D:
        print(cost_u)
        exit()

    if cost_u > min_cost[u]:
        continue

    for v in graph[u]:
        new_cost = cost_u + weights[v - 1]
        if new_cost < min_cost[v]:
            min_cost[v] = new_cost
            heapq.heappush(heap, (new_cost, v))


print(-1)