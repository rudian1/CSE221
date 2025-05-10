import heapq
def minimize_dngr(N, adj_list):
    dngr = [float('inf')] * (N + 1)
    dngr[1] = 0
    pq = [(0, 1)]  
    while pq:
        curr_dngr, u = heapq.heappop(pq)
        if curr_dngr > dngr[u]:
            continue
        for v, w in adj_list[u]:
            new_dngr = max(curr_dngr, w)
            if new_dngr < dngr[v]:
                dngr[v] = new_dngr
                heapq.heappush(pq, (dngr[v], v))
    return dngr
N, M = map(int, input().split())
adj_list = []
for i in range(N + 1):
    adj_list.append([])
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))
rslt = minimize_dngr(N, adj_list)
for i in range(1, N + 1):
    if rslt[i] == float('inf'):
        print(-1, end=' ')
    else:
        print(rslt[i], end=' ')
print()