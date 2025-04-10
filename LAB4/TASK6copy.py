numput1 = int(input())
x, y = map(int, input().split())

offset_row = [-1, 1, 0, 0, -1, -1, 1, 1]
offest_clmn = [0, 0, -1, 1, -1, 1, -1, 1]

moves_valid = []
for i in range(8):
    x_n = x + offset_row[i]  
    y_n = y + offest_clmn[i]  
    
    if 1 <= x_n <= numput1 and 1 <= y_n <= numput1:
        moves_valid.append((x_n, y_n))

moves_valid.sort()
print(len(moves_valid))
for move in moves_valid:
    print(move[0], move[1])