import sys

def diameter():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for i in range(N - 1):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    def bfs(start):
        visited = [-1] * (N + 1)
        queue = []
        front = 0
        queue.append(start)
        visited[start] = 0
        farthest_node = start
        max_distance = 0
        while front < len(queue):
            node = queue[front]
            front += 1
            for neighbor in adj[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
                    if visited[neighbor] > max_distance:
                        max_distance = visited[neighbor]
                        farthest_node = neighbor
        return farthest_node, max_distance
    
    node_A, _ = bfs(1)


    node_B, diameter = bfs(node_A)

    print(diameter)
    print(node_A, node_B)


diameter()