import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
cost = list([0]*3 for _ in range(N))
matrix = list([0]*3 for _ in range(N))

for i in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        cost[i][j] = value[j]


def func(n):
    for i in range(n):
        if i == 0 :
             matrix[i][0] = cost[i][0]
             matrix[i][1] = cost[i][1]
             matrix[i][2] = cost[i][2]
             continue
        matrix[i][0]= cost[i][0] + min(matrix[i-1][1],matrix[i-1][2])
        matrix[i][1]= cost[i][1] + min(matrix[i-1][0],matrix[i-1][2])
        matrix[i][2]= cost[i][2] + min(matrix[i-1][0],matrix[i-1][1])

    return min(matrix[n-1][0],matrix[n-1][1],matrix[n-1][2])
print(func(N))