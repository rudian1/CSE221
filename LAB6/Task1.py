N,M = map(int, input().split())
grph = []
for crs in range(N + 1):
    grph.append([])


in_dgr = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    grph[A].append(B)
    in_dgr[B] += 1


queue = []
for crs in range(1, N + 1):
    if in_dgr[crs] == 0:
        queue.append(crs)


index = 0
order = []
while index < len(queue):
    current = queue[index]
    index += 1
    order.append(current)

    for neighbor in grph[current]:
        in_dgr[neighbor] -= 1
        if in_dgr[neighbor] == 0:
            queue.append(neighbor)

if len(order) == N:
    for crs in order:
        print(crs, end=' ')
    print()
else:
    print(-1)