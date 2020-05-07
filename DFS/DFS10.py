import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
matrix = list([0]*(101) for _ in range(101))
visi = list()
for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    if not i in visi:
        visi.append(i)
    if not j in visi:
        visi.append(j)
    matrix[i][j] = 1
    matrix[j][i] = 1


def bfs(a):
    dis = list(0 for _ in range(101))
    visited.append(a)
    dis[a] = 1
    while visited:
        x = visited.popleft()
        for j in range(1,101):
            if matrix[x][j] == 1 and dis[j] == 0:
                visited.append(j)
                dis[j] = dis[x]+1
    answer = 0
    dis[a] = 0
    for i in visi:
            if dis[i] != 0 :
                answer += (dis[i]-1)
    return answer
        
    
sol = 5001
person = 1
for i in visi:
    visited = deque()
    ans = bfs(i)
    if ans == sol:
        if person>i:
            person = i

    elif ans < sol:
        sol = ans
        person = i
print(person)



