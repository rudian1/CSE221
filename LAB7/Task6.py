import heapq
def dijkstra(N, graph, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)] 
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        if current_dist > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist
def second_shortest_path(N, M, S, D, edges):
    
    graph = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    

    dist = dijkstra(N, graph, S)
    shortest_dist = dist[D]
    
    if shortest_dist == float('inf'):
        return -1
    
    second_shortest = float('inf')
    
    for u, v, w in edges:
        graph[u] = [pair for pair in graph[u] if pair != (v, w)]
        graph[v] = [pair for pair in graph[v] if pair != (u, w)]
        dist = dijkstra(N, graph, S)
        new_dist = dist[D]
        if new_dist > shortest_dist and new_dist < second_shortest:
            second_shortest = new_dist

        graph[u].append((v, w))
        graph[v].append((u, w))

    return second_shortest if second_shortest != float('inf') else -1

N, M, S, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]


result = second_shortest_path(N, M, S, D, edges)
print(result)