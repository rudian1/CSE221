Combined = input().split()
Numput1 = int(Combined[0])
numput2 = int(Combined[1])

numput3 = input().split()
numput4 = input().split()  

u = [int(x) for x in numput3]
v = [int(x) for x in numput4]

dgr = []
for i in range(Numput1 + 1):
    dgr.append(0)


for i in range(numput2):
    dgr[u[i]] += 1
    dgr[v[i]] += 1

odd_cnt = 0
for i in range(1, Numput1 + 1):
    if dgr[i] % 2 == 1:
        odd_cnt += 1

if odd_cnt == 0 or odd_cnt == 2:
    print("YES")
else:
    print("NO")