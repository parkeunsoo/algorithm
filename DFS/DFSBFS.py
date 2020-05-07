N, M, V = map(int,input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
queue = list()
c=[False for _ in range(N+1)]

for _ in range(M):
    link = list(map(int,input().split()))
    matrix[link[0]][link[1]]=1
    matrix[link[1]][link[0]]=1

def dfs(V):
    if c[V] == True:
        return True
    c[V] = True
    print(V,end='')
    for i in range(N+1):
        if matrix[V][i]==1:
            dfs(i)

def bfs(V,N):
    c=[False for _ in range(N+1)]
    queue.append(V)
    c[V] = True
    while queue:
        x = queue.pop(0)
        print(x,end='')
        for i in range(N+1):
            if matrix[x][i]==1:
                if not c[i]:
                    queue.append(i)
                    c[i] = True 
dfs(V)
bfs(V,N)


