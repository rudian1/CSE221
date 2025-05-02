N, M = map(int, input().split())
grph = []
for plr in range(N + 1):
    grph.append([])
for i in range(M):
    u, v = map(int, input().split())
    grph[u].append(v)
    grph[v].append(u)
clr = [0] * (N + 1)
max_group_size = 0  

for plr in range(1, N + 1):
    if clr[plr] == 0:
        que = [plr]
        clr[plr] = 1  
        index = 0

        g1 = 1  
        g2 = 0

        is_bipartite = True

        while index < len(que):
            current = que[index]
            index += 1

            for neighbor in grph[current]:
                if clr[neighbor] == 0:
                    if clr[current] == 1:
                        clr[neighbor] = 2
                        g2 += 1
                    else:
                        clr[neighbor] = 1
                        g1 += 1
                    que.append(neighbor)
                elif clr[neighbor] == clr[current]:
                    is_bipartite = False

        if is_bipartite:
            max_group_size += max(g1, g2)

print(max_group_size)