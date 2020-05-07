from collections import deque

M,N = map(int,input().split())
matrix = list([0]*M for _ in range(N))
dis = list([0]*M for _ in range(N))
start = list()
zero = list()
visited = list()
queue = deque()

for i in range(N):
    row = list(map(int,input().split()))
    for j in range(M):
        matrix[i][j] = row[j]
        if row[j] == 1:
            start.append((i,j))

def TOMATO():
    for (x,y) in start:
        queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        if x-1>=0 and matrix[x-1][y] == 0:
            queue.append((x-1,y))
            dis[x-1][y]=dis[x][y]+1
            matrix[x-1][y] = 1
        if y-1>=0 and matrix[x][y-1] == 0:
            queue.append((x,y-1))
            dis[x][y-1]=dis[x][y]+1
            matrix[x][y-1] = 1
        if x+1<N and matrix[x+1][y] == 0:
            queue.append((x+1,y))
            dis[x+1][y]=dis[x][y]+1
            matrix[x+1][y] = 1
        if y+1<M and matrix[x][y+1] == 0 :
            queue.append((x,y+1))
            dis[x][y+1]=dis[x][y]+1
            matrix[x][y+1] = 1
    for row in matrix:
        if 0 in row:
            return -1
    min_day=0
    for row in dis:
        min_day=max(min_day,max(row))
    return min_day

print(TOMATO())

