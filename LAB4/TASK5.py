Numput1, Numput2 = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

in_dgr = [0] * (Numput1 + 1)
out_dgr = [0] * (Numput1 + 1)

for i in range(Numput2):
    out_dgr[u[i]] += 1  
    in_dgr[v[i]] += 1

res = []
for i in range(1, Numput1 + 1):
    res.append(in_dgr[i] - out_dgr[i])

print(" ".join(map(str, res)))