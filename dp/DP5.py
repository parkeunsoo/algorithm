import sys 
N = int(sys.stdin.readline())
f = list([0]*N)
v = list()
for _ in range(N):
    v.append(int(sys.stdin.readline()))

def sol(n):
  
    if n < 3:
        if n == 0:
            return v[0]
        if n == 1:
            return v[1] + v[0]
        if n == 2:
            return max(v[0]+v[2],v[2]+v[1])
    else:
        f[0] = v[0]
        f[1] = v[1] + v[0]
        f[2] = max(v[0]+v[2],v[2]+v[1])
        for n in range(3,N):
            f[n] = max(f[n-2]+v[n],f[n-3]+v[n]+v[n-1])
    return f[n] 

print(sol(N-1))
