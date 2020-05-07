import sys

N = int(sys.stdin.readline())
matrix = list([0]*N for _ in range(N))
check = list([0]*N for _ in range(N))

for i in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        matrix[i][j]=value[j]

def dfs(s):
    visited.append(s)
    if c[s] == 1:
        return 
    c[s]= 1
    for i in range(N):
        if matrix[s][i] == 1:
            dfs(i)

for i in range(N):
    visited = list()
    c = list([0]*N)
    dfs(i)
    visited.pop(0)
    for j in range(N):
        if not j in visited:
            check[i][j] = 0
        else:
            check[i][j] = 1

for i in range(N):
    for j in range(N):
        print(check[i][j],end=" ")
    print()

