import sys
from collections import deque
M, N, H = map(int,sys.stdin.readline().split())

matrix = list(list([0]*(M) for _ in range(N)) for _ in range(H))
queue = deque()

for h in range(H):
    for i in range(N):
        value = list(map(int,sys.stdin.readline().split()))
        for j in range(M):
            matrix[h][i][j] = value[j]
            if matrix[h][i][j] == 1:
                queue.append((h,i,j))

def bfs(M,N,H):
    zero = True
    for row in matrix:
        for row in row:
            if 0 in row:
                zero = False
    if zero == True:
        return 0
    while queue:
        h,x,y = queue.popleft()
        if x-1 >= 0 and matrix[h][x-1][y] == 0:
            queue.append((h,x-1,y))
            matrix[h][x-1][y] = matrix[h][x][y]+1
        if y-1 >= 0 and matrix[h][x][y-1] == 0:
            queue.append((h,x,y-1))
            matrix[h][x][y-1] = matrix[h][x][y]+1
        if x+1 < N and matrix[h][x+1][y] == 0:
            queue.append((h,x+1,y))
            matrix[h][x+1][y] = matrix[h][x][y]+1
        if y+1 < M and  matrix[h][x][y+1] == 0:
            queue.append((h,x,y+1))
            matrix[h][x][y+1] = matrix[h][x][y]+1
        if h+1 < H and matrix[h+1][x][y] == 0:
            queue.append((h+1,x,y))
            matrix[h+1][x][y] = matrix[h][x][y]+1
        if h-1 >= 0 and matrix[h-1][x][y] == 0:
            queue.append((h-1,x,y))
            matrix[h-1][x][y] = matrix[h][x][y]+1

    for row in matrix:
        for row in row:
            if 0 in row:
                return -1
    min_day = 0
    for row in matrix:
        for row in row:
            min_day = max(min_day,max(row))
    return min_day-1

print(bfs(M,N,H))