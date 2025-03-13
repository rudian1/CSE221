import sys

def modular_exponentiation():
    
    inpu1, inpu2 = map(int, sys.stdin.readline().split())
    mod = 107

    res = 1
    base = inpu1 % mod  

    while inpu2 > 0:
        if inpu2 & 1:  
            res = (res * base) % mod
        base = (base * base) % mod  
        inpu2 >>= 1  
    
    sys.stdout.write(str(res) + "\n")

modular_exponentiation()