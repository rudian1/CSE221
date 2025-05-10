n, m, s, d = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))


g = []
for i in range(n + 1):
    g.append([])


for i in range(m):
    u = u_list[i]
    v = v_list[i]
    w = w_list[i]
    g[u].append((v, w))


def push(heap, node):
    heap.append(node)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent][0] > heap[i][0]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            break

def pop(heap):
    if not heap:
        return None
    root = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(heap) and heap[left][0] < heap[smallest][0]:
                smallest = left
            if right < len(heap) and heap[right][0] < heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
    return root

dist = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)
dist[s] = 0

heap = []
push(heap, (0, s))

while heap:
    cost, u = pop(heap)
    if cost > dist[u]:
        continue
    for v, w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            push(heap, (dist[v], v))

if dist[d] == float('inf'):
    print(-1)
else:
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(dist[d])
    print(' '.join(map(str, path)))
