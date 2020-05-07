import sys
from collections import deque
sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline())
sol= list()
def bfs(s):
    dis[s] = 1
    color[s] = True
    queue.append(s)
    while queue:
        x = queue.popleft()
        for i in matrix[x]:
            if dis[i] == 0:
                color[i] = not color[x]
                queue.append(i)
                dis[i] = dis[x]+1
            else:
                if color[i] == color[x]:
                    return False
    return True

for _ in range(K):
    V,E = map(int,sys.stdin.readline().split())
    queue = deque()
    color = list([0]*V)
    dis = list([0]*V)
    matrix = list([] for _ in range(V))

    for _ in range(E):
        x,y = map(int,sys.stdin.readline().split())
        matrix[x-1].append(y-1)
        matrix[y-1].append(x-1)
    for i in range(V):
        if dis[i] == 0:
            a = bfs(i)
            if a == False:
                sol.append("NO")
                break
    if a:
        sol.append("YES")
for i in range(K):
    print(sol[i])
    

