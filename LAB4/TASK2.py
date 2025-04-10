Numput1, Numput2 = map(int, input().split())
numput3 = list(map(int, input().split()))
numput4 = list(map(int, input().split()))
numput5 = list(map(int, input().split()))

adjcnt = {}
for i in range(1, Numput1 + 1):
    adjcnt[i] = []

for i in range(Numput2):
    adjcnt[numput3[i]].append((numput4[i], numput5[i]))

for i in range(1, Numput1+1):
    edges = ' '.join(f'({to},{wt})' for to, wt in adjcnt[i])
    print(f"{i}: {edges}")