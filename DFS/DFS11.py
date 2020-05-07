import sys
sys.setrecursionlimit(10**6)
K = int(sys.stdin.readline())
answer = list()
a = False
def dfs(s,V):
    global a
    if s in visit:
        return
    visit.append(s)
    for i in matrix[s]:
        if i in visit:
            if color[i] == color[s]:
                a=True

        elif i not in visit:
            color[i] = not color[s]
            dfs(i,V)
            
for _ in range(K):
    V,E = map(int,sys.stdin.readline().split())
    visit = list()
    color = list([True]*(V))
    test = list()
    matrix = list([] for _ in range(V))
    count = 0

    for _ in range(E):
        x,y = map(int,sys.stdin.readline().split())
        matrix[x-1].append(y-1)
        matrix[y-1].append(x-1)
    for i in range(V):
        if i not in visit:
            dfs(i,V)
            if a:
                answer.append("NO")
                break
    if not a:
        answer.append("YES")
for i in range(K):
    print(answer[i])


