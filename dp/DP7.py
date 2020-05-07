import sys
N = int(sys.stdin.readline())
V = list([0]*N for _ in range(N))
dp = list([0]*N for _ in range(N))
for i in range(N):
    value = list(map(int,sys.stdin.readline().split()))
    for j in range(len(value)):
        V[i][j] = value[j]

for i in range(N):
    for j in range(N):
        if i == 0:
            dp[i][j]=V[i][j]
        dp[i][j] = V[i][j]+max(dp[i-1][j-1],dp[i-1][j])
answer = 0
for value in dp[N-1]:
    answer = max(answer,value)

print(answer)