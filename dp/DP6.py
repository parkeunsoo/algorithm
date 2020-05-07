import sys
N = int(sys.stdin.readline())
f = list([0]*91)
g = list([0]*91)
sol = list([0]*91)

def answer(N):
    f[3]=1
    g[3]=1
    sol[1]=1
    sol[2]=1
    sol[3]=2
    for i in range(4,N+1):
        f[i] = sol[i-1]
        g[i] = f[i-1]
        sol[i] = f[i] + g[i]
    return sol[N]

print(answer(N))