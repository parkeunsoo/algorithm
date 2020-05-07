import sys
import copy
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
matrix = list([0]*N for _ in range(N))
check1 = list([0]*N for _ in range(N))
check2 = list([0]*N for _ in range(N))
for i in range(N):
    value = list(sys.stdin.readline())
    for j in range(N):
        matrix[i][j] = value[j]

def dfs1(x,y):
    if check1[x][y]==True:
        return 
    check1[x][y]=True
    if x-1>=0 and check1[x-1][y] == 0 and matrix[x][y] == matrix[x-1][y]:
        dfs1(x-1,y)
    if y-1>=0 and check1[x][y-1] == 0 and matrix[x][y] == matrix[x][y-1]:
        dfs1(x,y-1)
    if x+1<N and check1[x+1][y] == 0 and matrix[x][y] == matrix[x+1][y]:
        dfs1(x+1,y)
    if y+1<N and check1[x][y+1] == 0 and matrix[x][y] == matrix[x][y+1]:
        dfs1(x,y+1)

def dfs2(x,y,C):
    if check2[x][y]==True:
        return 
    check2[x][y]=True
    if C == 'R'or C =='G':
        if x-1>=0 and check2[x-1][y] == 0 and (matrix[x-1][y] == 'R' or matrix[x-1][y] == 'G'):
            dfs2(x-1,y,matrix[x-1][y])
        if y-1>=0 and check2[x][y-1] == 0 and (matrix[x][y-1] == 'R' or matrix[x][y-1] == 'G'):
            dfs2(x,y-1,matrix[x][y-1])
        if x+1<N and check2[x+1][y] == 0 and (matrix[x+1][y] == 'R' or matrix[x+1][y] == 'G'):
            dfs2(x+1,y,matrix[x+1][y])
        if y+1<N and check2[x][y+1] == 0 and (matrix[x][y+1] == 'R' or matrix[x][y+1] == 'G'):
            dfs2(x,y+1,matrix[x][y+1])
    else:
        if x-1>=0 and check2[x-1][y] == 0 and matrix[x-1][y] == 'B':
            dfs2(x-1,y,matrix[x-1][y])
        if y-1>=0 and check2[x][y-1] == 0 and matrix[x][y-1] == 'B':
            dfs2(x,y-1,matrix[x][y-1])
        if x+1<N and check2[x+1][y] == 0 and matrix[x+1][y] == 'B':
            dfs2(x+1,y,matrix[x+1][y])
        if y+1<N and check2[x][y+1] == 0 and matrix[x][y+1] == 'B':
            dfs2(x,y+1,matrix[x][y+1])

count1 = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if check1[i][j] == 0:
            dfs1(i,j)
            count1 += 1
        if check2[i][j] == 0:
            dfs2(i,j,matrix[i][j])
            count2 += 1
print(count1, count2)
