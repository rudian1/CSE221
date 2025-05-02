import sys
sys.setrecursionlimit(1 << 20)
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
wrds = []
for i in range(N):
    wrds.append(input().strip())


grph = []
for i in range(26):
    grph.append([])


in_dgr = [0] * 26
used = [False] * 26
invalid = False


for i in range(N - 1):
    w1 = wrds[i]
    w2 = wrds[i + 1]
    min_len = min(len(w1), len(w2))
    found = False

    for j in range(min_len):
        if w1[j] != w2[j]:
            a = ord(w1[j]) - ord('a')
            b = ord(w2[j]) - ord('a')
            grph[a].append(b)
            in_dgr[b] += 1
            found = True
            break

    if not found and len(w1) > len(w2):
        invalid = True
        break

for word in wrds:
    for ch in word:
        used[ord(ch) - ord('a')] = True


if invalid:
    print(-1)
else:
    order = []
    queue = []

    for i in range(26):
        if used[i] and in_dgr[i] == 0:
            queue.append(i)

    queue.sort()  

    head = 0
    while head < len(queue):
        current = queue[head]
        order.append(current)
        head += 1

        next_nodes = grph[current]
        for neighbor in next_nodes:
            in_dgr[neighbor] -= 1


        new_zero = []
        for neighbor in next_nodes:
            if in_dgr[neighbor] == 0:
                new_zero.append(neighbor)

        new_zero.sort()
        for node in new_zero:
            if node not in queue[head:]:  
                queue.append(node)

    if len(order) != sum(used):
        print(-1)
    else:
        for i in order:
            print(chr(i + ord('a')), end='')
        print()