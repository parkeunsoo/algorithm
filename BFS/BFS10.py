import sys
from collections import deque
N = int(sys.stdin.readline())
matrix = list([0]*N for _ in range(N))
dis = list([0]*N)
s,e = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())
queue = deque()
for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

def bfs(s,e):
    queue.append(s)
    dis[s] = 1
    while queue:
        x = queue.popleft()
        for i in range(N):
            if matrix[x][i] == 1 and dis[i] == 0:
                queue.append(i)
                dis[i] = dis[x] + 1
                if i == e:
                    return dis[e]-1
    return -1

print(bfs(s-1,e-1))