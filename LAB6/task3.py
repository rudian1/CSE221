import sys

def solve():
    N = int(sys.stdin.readline())
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    visited = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]
    
    
    que = []
    f = 0
    b = 0
    que.append((x1, y1))
    b += 1
    visited[x1][y1] = 0
    
    while f < b:
        x, y = que[f]
        f += 1
        if x == x2 and y == y2:
            print(visited[x][y])
            return
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= N and 1 <= ny <= N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                b += 1
    
    print(-1)


solve()