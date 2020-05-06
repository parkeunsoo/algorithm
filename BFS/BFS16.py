#1600
import sys
from collections import deque

K = int(sys.stdin.readline())
W, H = map(int,sys.stdin.readline().split())
matrix = list([]for _ in range(H))
for i in range(H):
    matrix[i] = list(map(int,sys.stdin.readline().split()))
visit = list([[-1]*(K+1) for _ in range(W)] for _ in range(H))
queue = deque()
queue.append((0,0,0,K))
def bfs():
    dis = 0
    while queue:
        x, y, dis, count = queue.popleft()
        if x == H-1 and y == W-1:
            return dis
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx = x+dx
            ny = y+dy
            if nx < 0 or ny < 0 or nx >= H or ny >= W or matrix[nx][ny] == 1 or visit[nx][ny][count] != -1 :
                continue
            queue.append((nx,ny,dis+1,count))
            visit[nx][ny][count] = 0
        
        if count > 0 :
            for dx,dy in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
                nx = x+dx
                ny = y+dy
                if nx < 0 or ny < 0 or nx >= H or ny >= W or matrix[nx][ny] == 1 or visit[nx][ny][count-1] != -1 :
                continue
                queue.append((nx,ny,dis+1,count-1))
                visit[nx][ny][count-1] = 0
    return -1                    

print(bfs())

        
        





