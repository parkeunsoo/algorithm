import sys
from collections import deque
N = int(sys.stdin.readline()) 
node = list([]for _ in range(N+1))
queue = deque()
for i in range(N-1):
    value = list(map(int,sys.stdin.readline().split()))
    node[value[0]].append((value[1],value[2]))
    node[value[1]].append((value[0],value[2]))

def bfs(s):
    dis = list([0]*(N+1))
    queue.append(s)
    while queue:
        x = queue.popleft()
        for j in node[x]: 
            i = j[0]
            if dis[i] == 0 :
                queue.append(i)
                dis[i] = dis[x] + j[1]
    return max(dis)

maxn = 0
for i in range(1,N+1):
    dis = bfs(i)
    if maxn < dis:
        maxn = dis
print(maxn)
    


