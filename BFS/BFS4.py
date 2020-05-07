import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
queue = deque()
po = list([0]*100001)
dis = list([0]*100001)

def f(N,K):
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            return dis[x]
        if  x+1 <= 100000 and po[x+1] == 0:
            po[x+1] = 1
            queue.append(x+1)
            dis[x+1] = dis[x]+1
        if  x-1 >= 0 and po[x-1] == 0:
            po[x-1] = 1
            queue.append(x-1)
            dis[x-1] = dis[x]+1
        if  2*x <= 100000 and po[2*x] == 0 and not x==0:
            po[2*x] = 1
            queue.append(2*x)
            dis[2*x] = dis[x]+1
   
print(f(N,K))