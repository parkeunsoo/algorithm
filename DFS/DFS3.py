import sys
sys.setrecursionlimit(100000)

def abc():
    number = 0
    for _ in range(K):
        i,j = map(int,input().split())
        matrix[i][j] = 1
    for i in range(N):
        for j in range(M):
            if not (i,j) in visited and matrix[i][j] == 1:
                dfs(i,j)
                number += 1
    count.append(number)

def dfs(x,y):
    if (x,y) in visited:
        return
    visited.append((x,y))
    if x-1 >= 0 and matrix[x-1][y] == 1:
        dfs(x-1,y)
    if y-1 >= 0 and matrix[x][y-1] == 1:
        dfs(x,y-1)
    if x+1 < N and matrix[x+1][y] == 1:
        dfs(x+1,y)
    if y+1 < M and matrix[x][y+1] == 1:
        dfs(x,y+1)

T = int(input())
count = list()

for i in range(T):
    N, M, K = map(int,input().split())
    matrix = list([0]*M for _ in range(N))
    visited = list()
    abc()
for i in range(T):
    print(count[i])