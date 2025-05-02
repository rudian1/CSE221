N,M = map(int, input().split())
graph = []
for course in range(N + 1):
    graph.append([])


indegree = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


queue = []
for course in range(1, N + 1):
    if indegree[course] == 0:
        queue.append(course)


index = 0
order = []
while index < len(queue):
    current = queue[index]
    index += 1
    order.append(current)

    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(order) == N:
    for course in order:
        print(course, end=' ')
    print()
else:
    print(-1)