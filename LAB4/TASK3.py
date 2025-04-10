Numput1 = int(input())
mtx = [[0 for i in range(Numput1)] for i in range(Numput1)]
for i in range(Numput1):
    prts = list(map(int, input().split()))
    y = prts[0]
    neighbors = prts[1:]
    for neighbor in neighbors:
        mtx[i][neighbor] = 1

for row in mtx:
    row_str = ''
    for val in row:
        row_str += str(val) + ' '
    print(row_str.strip())