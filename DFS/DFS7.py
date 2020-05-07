import sys
import copy
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
maxvalue = 0
matrix = list([0]*N for _ in range(N))
visited = list()
f = list([0]*N for _ in range(N))   
for i in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        matrix[i][j] = value[j]
        if maxvalue < value[j]:
            maxvalue = value[j]
        

def sol(maxvalue):
    global f
    global visited
    maxi = 0
    for i in range(1,maxvalue):
        count = 0
        f = list([0]*N for _ in range(N))    
        for j in range(N):
            for k in range(N):
                if matrix[j][k] < i:
                    f[j][k] = 2
        for n in range(N):
            for m in range(N):
                if f[n][m] == 0:
                    dfs(n,m)
                    count += 1
                    visited = list()
        if maxi<count:
            maxi = count
    return maxi

def dfs(x,y):
    if (x,y) in visited:
        return 
    visited.append((x,y))
    if x-1 >= 0 and f[x-1][y] == 0:
        f[x-1][y]=1
        dfs(x-1,y)
    if y-1 >= 0 and f[x][y-1] == 0:
        f[x][y-1]=1
        dfs(x,y-1)
    if x+1 < N and f[x+1][y] == 0:
        f[x+1][y]=1
        dfs(x+1,y)
    if y+1 < N and f[x][y+1] == 0:
        f[x][y+1]=1
        dfs(x,y+1)

print(sol(maxvalue))
    
