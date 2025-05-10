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
        pair = self.data.pop()
        self._sift_down(0)
        return pair

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.data[p][0] > self.data[i][0]:
                self._swap(p, i)
                i = p
            else:
                break

    def _sift_down(self, i):
        size = len(self.data)
        while 2 * i + 1 < size:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if self.data[l][0] < self.data[smallest][0]:
                smallest = l
            if r < size and self.data[r][0] < self.data[smallest][0]:
                smallest = r
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

        
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def is_empty(self):
        return len(self.data) == 0
    
N, M = map(int, input().split())
adj_list = []
for i in range(N + 1):
    adj_list.append([])
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

dngr = [float('inf')] * (N + 1)
dngr[1] = 0
heap = MinHeap()
heap.push((0, 1))

while not heap.is_empty():
    curr_d, u = heap.pop()
    if curr_d > dngr[u]:
        continue
    for v, w in adj_list[u]:
        max_d = max(dngr[u], w)
        if max_d < dngr[v]:
            dngr[v] = max_d
            heap.push((dngr[v], v))


output = ""
for i in range(1, N + 1):
    if dngr[i] == float('inf'):
        output += "-1 "
    else:
        output += str(dngr[i]) + " "
print(output.strip())