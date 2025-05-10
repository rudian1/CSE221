N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))


g = []
for _ in range(N + 1):
    g.append([])

for i in range(M):
    g[u[i]].append((v[i], w[i]))

INF = 1 << 60
dist = [[INF, INF] for _ in range(N + 1)]
dist[1][0] = 0
dist[1][1] = 0
que = [(0, 1, -1)]


while que:
    idx = min(range(len(que)), key=lambda i: que[i][0])
    cost, node, last_parity = que.pop(idx)

    for neighbor, weight in g[node]:
        parity = weight % 2
        if last_parity == -1 or parity != last_parity:
            new_cost = cost + weight
            if new_cost < dist[neighbor][parity]:
                dist[neighbor][parity] = new_cost
                que.append((new_cost, neighbor, parity))


result = min(dist[N][0], dist[N][1])
print(result if result != INF else -1)