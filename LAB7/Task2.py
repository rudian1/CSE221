class MinHeap:
    def __init__(self):
        self.data = []
    def push(self, pair):
        self.data.append(pair)
        self._sift_up(len(self.data) - 1)
    def pop(self):
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        min_pair = self.data.pop()
        self._sift_down(0)
        return min_pair
    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent][0] > self.data[i][0]:
                self._swap(parent, i)
                i = parent
            else:
                break
    def _sift_down(self, i):
        size = len(self.data)
        while 2 * i + 1 < size:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if self.data[left][0] < self.data[smallest][0]:
                smallest = left
            if right < size and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    def is_empty(self):
        return len(self.data) == 0 
def dijkstra(N, adj_list, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = MinHeap()
    heap.push((0, start))
    while not heap.is_empty():
        d, u = heap.pop()
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heap.push((dist[v], v))
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