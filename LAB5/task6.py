row = input().split()
r = int(row[0])
h = int(row[1])

clmn = []
for i in range(r):
    row = input()
    clmn.append(list(row)) 


visit = []
for i in range(r):
    visit.append([False] * h)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 


mx_dmnd = 0
for i in range(r):
    for j in range(h):
        if visit[i][j] == False and clmn[i][j] != '#':
            # Begin BFS
            queue = []
            queue.append([i, j])
            visit[i][j] = True

            diamonds = 0
            if clmn[i][j] == 'D':
                diamonds = 1

            while len(queue) > 0:
                current = queue[0]
                del queue[0]
                x = current[0]
                y = current[1]

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx >= 0 and nx < r and ny >= 0 and ny < h:
                        if visit[nx][ny] == False and clmn[nx][ny] != '#':
                            visit[nx][ny] = True
                            if clmn[nx][ny] == 'D':
                                diamonds = diamonds + 1
                            queue.append([nx, ny])

            # Update max diamonds
            if diamonds > mx_dmnd:
                mx_dmnd = diamonds


print(mx_dmnd)