import sys
N = int(sys.stdin.readline())
dp = list([1]*10 for _ in range(N+1))


for i in range(2,N+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
answer = 0
for row in dp[N][1:10]:
    answer += row
print((answer)%1000000000)
