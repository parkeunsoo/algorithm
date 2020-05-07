import sys
from collections import deque
N = int(sys.stdin.readline())
control = list([0]*3 for _ in range(N))
start = list()
queue = deque()
for i in range(N):
    control[i][0] = int(sys.stdin.readline())
    control[i][1] = tuple(map(int,sys.stdin.readline().split()))
    control[i][2] = tuple(map(int,sys.stdin.readline().split()))


def bfs(a,b,N,dis):
    
    while queue:
        x,y = queue.popleft()
        if x+1 < N and y+2 < N and dis[x+1][y+2] == 0:
            queue.append((x+1,y+2))
            dis[x+1][y+2] = dis[x][y] + 1
        if x+2 < N and y+1 < N and dis[x+2][y+1] == 0:
            queue.append((x+2,y+1))
            dis[x+2][y+1] = dis[x][y] + 1
        if x+2 < N and y-1 >= 0 and dis[x+2][y-1] == 0:
            queue.append((x+2,y-1))
            dis[x+2][y-1] = dis[x][y] + 1
        if x+1 < N and y-2 >= 0 and dis[x+1][y-2] == 0:
            queue.append((x+1,y-2))
            dis[x+1][y-2] = dis[x][y] + 1
        if x-2 >= 0 and y-1 >= 0 and dis[x-2][y-1] == 0:
            queue.append((x-2,y-1))
            dis[x-2][y-1] = dis[x][y] + 1
        if x-1 >= 0 and y-2 >= 0 and dis[x-1][y-2] == 0:
            queue.append((x-1,y-2))
            dis[x-1][y-2] = dis[x][y] + 1
        if x-2 >= 0 < N and y+1 < N and dis[x-2][y+1] == 0:
            queue.append((x-2,y+1))
            dis[x-2][y+1] = dis[x][y] + 1
        if x-1 >= 0 < N and y+2 < N and dis[x-1][y+2] == 0:
            queue.append((x-1,y+2))
            dis[x-1][y+2] = dis[x][y] + 1
    return dis[a][b]-1


for i in range(N):
    num = control[i][0]
    a,b = control[i][1]
    c,d = control[i][2]
    dis = list([0]*num for _ in range(num))
    dis[a][b] = 1
    queue.append((a,b))
    print(bfs(c,d,num,dis))