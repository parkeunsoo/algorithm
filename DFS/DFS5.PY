import sys
from collections import deque
sys.setrecursionlimit(10**6)
N, M = map(int,sys.stdin.readline().split())
matrix = list([0]*N for _ in range(N))
visited = list([False]*N)
count = 0

def dfs(x):
    if visited[x] == True:
        return 0
    visited[x] = True
    for j in range(N):
        if matrix[x][j] == 1:
            dfs(j)
    return 1

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1


for i in range(N):
    a = dfs(i)
    count += a

print(count)