Numput1 = int(input())
fst, snd = map(int, input().split())

moves = [
    (fst-1, snd),     # Up
    (fst+1, snd),     # Down
    (fst, snd-1),     # Left
    (fst, snd+1),     # Right
    (fst-1, snd-1),   # Top-left diagonal
    (fst-1, snd+1),   # Top-right diagonal
    (fst+1, snd-1),   # Bottom-left diagonal
    (fst+1, snd+1)    # Bottom-right diagonal
]

moves_valid = []
for x_n, y_n in moves:
    if 1 <= x_n <= Numput1 and 1 <= y_n <= Numput1:
        moves_valid.append((x_n, y_n))

moves_valid.sort()

print(len(moves_valid))
for move in moves_valid:
    print(move[0], move[1])