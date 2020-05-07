import sys
T = int(sys.stdin.readline())
number = list()
f = list([0]*41)
g = list([0]*41)

def zero(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        if f[n] != 0:
            return f[n]
        else:
            f[n] = zero(n-1)+zero(n-2)
            return f[n]
def one(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if g[n] != 0:
            return g[n]
        else:
            g[n] = one(n-1)+one(n-2)
            return g[n]
    
for _ in range(T):
    number.append(int(sys.stdin.readline()))
for i in range(T):
    print(zero(number[i]),one(number[i]))