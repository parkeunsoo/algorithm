import sys
from collections import deque
sys.setrecursionlimit(10**6)
R,C = map(int,sys.stdin.readline().split())
matrix = list([0]*C for _ in range(R))
visited = deque()
check = list()
for i in range(R):
    value = list(sys.stdin.readline())
    for j in range(C):
        matrix[i][j] = value[j]
count = 0
def dfs(x,y,count):
    global visited
    global answer
    answer = max(answer,count)
    visited.append(matrix[x][y])
    if x-1>=0 and matrix[x-1][y] not in visited:
        dfs(x-1,y,count+1)
        visited.remove(matrix[x-1][y])
    if y-1>=0 and matrix[x][y-1] not in visited:
        dfs(x,y-1,count+1)
        visited.remove(matrix[x][y-1])
    if x+1<R and matrix[x+1][y] not in visited:
        dfs(x+1,y,count+1)
        visited.remove(matrix[x+1][y])
    if y+1<C and matrix[x][y+1] not in visited:
        dfs(x,y+1,count+1)
        visited.remove(matrix[x][y+1])
answer=1
dfs(0,0,1)
print(answer)
