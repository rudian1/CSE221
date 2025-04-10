Numput1, Numput2 = map(int, input().split())
matrix_adjcnt = [[0] * Numput1 for _ in range(Numput1)]
for i in range(Numput2):
    numput3, numput4, numput5 = map(int, input().split())
    matrix_adjcnt[numput3 - 1][numput4 - 1] = numput5
for row in matrix_adjcnt:
    print(' '.join(map(str, row)))