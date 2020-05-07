import sys

N, M = map(int,sys.stdin.readline().split())
dp = list([0]*(N+1) for _ in range(M+1))
for i in range(1,M+1):
    dp[i][1] = i-1
    for j in range(2,N+1):
        dp[i][j] = dp[i][j-1] + dp[i][1] + 1
print(dp[M][N])