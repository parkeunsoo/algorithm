import sys
from collections import deque
R,C = map(int,sys.stdin.readline().split())
matrix = list(['.']*C for _ in range(R))
dis = list([0]*C for _ in range(R))
queue = list()
home = deque()
for i in range(R):
    row = list(sys.stdin.readline())
    for j in range(C):
        matrix[i][j] = row[j]
        if row[j] == 'S' or row[j] == '*':
            queue.append((row[j],i,j))
            dis[i][j] = 1
        if row[j] == 'D':
            home.append((i,j))

queue.sort()
def bfs():
    while queue:
        v,x,y = queue.pop(0)
        if v == '*':
            if x+1 < R and matrix[x+1][y] == '.':
                matrix[x+1][y] = '*'
                queue.append(('*',x+1,y))
            if y+1 < C and matrix[x][y+1] == '.':
                matrix[x][y+1] = '*'
                queue.append(('*',x,y+1))
            if x-1 >= 0 and matrix[x-1][y] == '.':
                matrix[x-1][y] = '*'
                queue.append(('*',x-1,y))
            if y-1 >= 0 and matrix[x][y-1] == '.':
                matrix[x][y-1] = '*'
                queue.append(('*',x,y-1))
        elif v == 'S':
            if x+1 < R and dis[x+1][y] == 0 and (matrix[x+1][y] == '.' or matrix[x+1][y] == 'D'):
                dis[x+1][y] = dis[x][y] + 1
                queue.append(('S',x+1,y))
            if y+1 < C and dis[x][y+1] == 0 and (matrix[x][y+1] == '.'or matrix[x][y+1] == 'D'):
                dis[x][y+1] = dis[x][y] + 1
                queue.append(('S',x,y+1))
            if x-1 >= 0 and dis[x-1][y] == 0 and (matrix[x-1][y] == '.'or matrix[x-1][y] == 'D'):
                dis[x-1][y] = dis[x][y] + 1
                queue.append(('S',x-1,y))
            if y-1 >= 0 and dis[x][y-1] == 0 and (matrix[x][y-1] == '.'or matrix[x][y-1] == 'D'):
                dis[x][y-1] = dis[x][y] + 1
                queue.append(('S',x,y-1))
bfs()
x,y = home.popleft()
if dis[x][y] == 0:
    print("KAKTUS")
else:
    print(dis[x][y]-1)
