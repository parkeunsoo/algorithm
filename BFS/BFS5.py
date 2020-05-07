import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
matrix = list([0]*N for _ in range(N))
queue = deque()
visited = list([False]*N)
count = 0

def bfs(i):
    if visited[i] == True:
        return 0
    visited[i] = True
    queue.append(i)
    while queue:
        x = queue.popleft() 
        for j in range(N):
            if j not in queue and matrix[x][j] == 1 and visited[j] == False:
                queue.append(j)
                visited[j] = True
    return 1

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1


for i in range(N):
    a = bfs(i)
    count += a

print(count)