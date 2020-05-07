import sys
from collections import deque
queue = deque()
F,S,G,U,D = map(int,sys.stdin.readline().split())
s = [None]*(F+1)
def sol(F,S,G,U,D):
    queue.append(S)
    s[S] = 1
    while queue:
        x = queue.popleft()
        if x == G:
            return s[G] -1 
        if x+U < F+1 and not s[x+U]:
            s[x+U] = s[x]+1
            queue.append(x+U)
        if x-D > 0 and not s[x-D]:
            s[x-D] = s[x]+1
            queue.append(x-D)
    return "use the stairs"
print(sol(F,S,G,U,D))