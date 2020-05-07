import sys
import copy
from collections import deque
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())
matrix = list([0]*M for _ in range(N))
newb = list()
start = list()
queue = deque()

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        matrix[i][j] = row[j]
        if matrix[i][j] == 0:
            newb.append((i,j))
        if matrix[i][j] == 2:
            start.append((i,j))

comb = list(combinations(newb,3))
num = len(comb)
answer = 0
def number(matrix):
    global answer
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                count += 1
    if answer < count:
        answer = count

def bfs(matrix):
    for i,j in start:
        queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        if x-1>=0 and (x-1,y) not in queue and matrix[x-1][y] == 0:
            matrix[x-1][y] = 2
            queue.append((x-1,y))
        if y-1>=0 and (x,y-1) not in queue and matrix[x][y-1] == 0:
            matrix[x][y-1] = 2
            queue.append((x,y-1))
        if x+1<N and (x+1,y) not in queue and matrix[x+1][y] == 0:
            matrix[x+1][y] = 2
            queue.append((x+1,y))
        if y+1<M and (x,y+1) not in queue and matrix[x][y+1] == 0:
            matrix[x][y+1] = 2
            queue.append((x,y+1))



for i in range(num):
    copy_matrix = copy.deepcopy(matrix)
    for j in range(3):
        x,y = comb[i][j]
        copy_matrix[x][y] = 1
    bfs(copy_matrix)
    number(copy_matrix)
print(answer)




        