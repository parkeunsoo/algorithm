#11057
import sys
n = int(sys.stdin.readline())

dp = list([0]*(11) for _ in range(n+1))

for i in range(1,n+1):
    for j in range(1,11):
        if i == 1 :
            dp[i][j] = j
        else:
            s = 0
            for k in range(j+1):
                s += dp[i-1][k]
            dp[i][j] = s

print(dp[n][10]%10007)
