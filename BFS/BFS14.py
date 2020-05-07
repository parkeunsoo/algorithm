import sys
import copy
from collections import deque
N, M = map(int,sys.stdin.readline().split())
matrix = list([0]*M for _ in range(N))
queu = list()
queue = deque()
dis = list([-1]*M for _ in range(N))
for i in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        matrix[i][j] = value[j]
        if value[j] != 0:
            queu.append((i,j))
            dis[i][j] = 0

def melt():
    for x,y in queu:
        if x+1 < N and matrix[x+1][y] == 0 and matrixx[x][y] > 0:
            matrixx[x][y] -= 1
        if y+1 < M and matrix[x][y+1] == 0 and matrixx[x][y] > 0:
            matrixx[x][y] -= 1
        if x-1 >= 0 and matrix[x-1][y] == 0 and matrixx[x][y] > 0:
            matrixx[x][y] -= 1
        if y-1 >= 0 and matrix[x][y-1] == 0 and matrixx[x][y] > 0:
            matrixx[x][y] -= 1
      
def bfs():
    x,y = queu[0]
    queue.append((x,y))
    diss[x][y] = 1
    while queue:
        x,y = queue.popleft()
        if x+1 < N and diss[x+1][y] == 0 and matrixx[x+1][y] != 0:
            queue.append((x+1,y))
            diss[x+1][y] = diss[x][y]+1
        if y+1 < M and diss[x][y+1] == 0 and matrixx[x][y+1] != 0:
            queue.append((x,y+1))
            diss[x][y+1] = diss[x][y]+1
        if x-1 >= 0 and diss[x-1][y] == 0 and matrixx[x-1][y] != 0:
            queue.append((x-1,y))
            diss[x-1][y] = diss[x][y]+1
        if y-1 >= 0 and diss[x][y-1] == 0 and matrixx[x][y-1] != 0:
            queue.append((x,y-1))
            diss[x][y-1] = diss[x][y]+1
answer = -1
count = 0
while True:
    sol = 0
    matrixx = copy.deepcopy(matrix)
    melt()
    matrix = matrixx
    diss = copy.deepcopy(dis)
    bfs()
    count += 1
    for x,y in queu:
        if diss[x][y] == 0 and matrixx[x][y] >0:
            answer = count 
            print(answer)
            break
        if matrixx[x][y] != 0:
            sol += 1
    if answer != -1:
        break
    if sol == 0:
        print(sol)
        break  
    