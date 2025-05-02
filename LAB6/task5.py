from collections import deque

def find_farthest_node(start, graph, n):
    visited = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    farthest_node = start
    max_distance = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor
    return farthest_node, max_distance


def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input[ptr])
        v = int(input[ptr + 1])
        ptr += 2
        graph[u].append(v)
        graph[v].append(u)
    
    node, _ = find_farthest_node(1, graph, n)
    other_node, diameter = find_farthest_node(node, graph, n)
    print(diameter)
    print(node, other_node)


if __name__ == "__main__":
    main()