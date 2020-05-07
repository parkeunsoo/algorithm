N,M = map(int,input().split())
dis = list([0]*M for _ in range(N))
matrix = list([0]*M for _ in range(N))
queue = list()
visited = list()

for i in range(N):
    value = list(map(int,input()))
    for j in range(M):
        matrix[i][j] = value[j]

def BFS(N,M):
    dis[0][0] = 0
    queue.append((0,0))
    while queue:
        x,y=queue.pop(0)
        visited.append((x,y))
        if x==N-1 and y==M-1 :
            break
        if y+1<M and (x,y+1) not in queue and (x,y+1) not in visited and matrix[x][y+1] == 1:
            dis[x][y+1] = dis[x][y] + 1
            queue.append((x,y+1))
        if x+1<N and (x+1,y) not in queue and (x+1,y) not in visited and matrix[x+1][y] == 1:
            dis[x+1][y] = dis[x][y] + 1
            queue.append((x+1,y))
        if x>0 and (x-1,y) not in queue and (x-1,y) not in visited and matrix[x-1][y] == 1:
            dis[x-1][y] = dis[x][y] + 1
            queue.append((x-1,y))
        if y>0 and (x,y-1) not in queue and (x,y-1) not in visited and matrix[x][y-1] == 1:
            dis[x][y-1] = dis[x][y] + 1
            queue.append((x,y-1))
    return dis[N-1][M-1] + 1

print(BFS(N,M))