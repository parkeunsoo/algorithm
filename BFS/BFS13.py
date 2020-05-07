import sys
from collections import deque
N, M  = map(int,sys.stdin.readline().split())
matrix = list([0]*M for _ in range(N))
queue = deque()
for i in range(N):
    value = list(sys.stdin.readline())
    for j in range(M):
        matrix[i][j] = value[j]

def bfs(i,j):
    dis = list([-1]*M for _ in range(N))
    queue.append((i,j))
    dis[i][j] = 0
    while queue:
        x,y = queue.popleft()
        if x-1 >= 0 and matrix[x-1][y] =='L'and dis[x-1][y] == -1:
            queue.append((x-1,y))
            dis[x-1][y] = dis[x][y] + 1
        if x+1 < N and matrix[x+1][y] =='L'and dis[x+1][y] == -1:
            queue.append((x+1,y))
            dis[x+1][y] = dis[x][y] + 1
        if y-1 >= 0 and matrix[x][y-1] =='L'and dis[x][y-1] == -1:
            queue.append((x,y-1))
            dis[x][y-1] = dis[x][y] + 1
        if y+1 < M and matrix[x][y+1] =='L'and dis[x][y+1] == -1:
            queue.append((x,y+1))
            dis[x][y+1] = dis[x][y] + 1
    min_day=0
    for row in dis:
        min_day=max(min_day,max(row))
    return min_day
        
maxn = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'L':
            sol = bfs(i,j)
            if sol > maxn:
                maxn = sol
        
print(maxn)




