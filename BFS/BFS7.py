import sys
from collections import deque

M, N, K = map(int,sys.stdin.readline().split())
matrix = list([0]*N for _ in range(M))
queue = deque()
answer = list()
sol = 0

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            matrix[i][j]=2

def bfs(n,m):
    count = 0
    queue.append((n,m))
    matrix[n][m]= 1
    while queue:
        x,y = queue.popleft()
        count += 1
        if x-1 >= 0 and (x-1,y) not in queue and matrix[x-1][y] == 0:
            matrix[x-1][y] = 1
            queue.append((x-1,y))
        if y-1 >= 0 and (x,y-1) not in queue and matrix[x][y-1] == 0:
            matrix[x][y-1] = 1
            queue.append((x,y-1))
        if x+1 < M and (x+1,y) not in queue and matrix[x+1][y] == 0:
            matrix[x+1][y] = 1
            queue.append((x+1,y))
        if y+1 < N and (x,y+1) not in queue and matrix[x][y+1] == 0:
            matrix[x][y+1] = 1
            queue.append((x,y+1))
    return count

for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            answer.append(bfs(i,j))
            sol += 1

            
answer.sort()
print(sol)
for value in answer:
    print(value,end=" ")
        
