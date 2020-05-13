#1699
import sys
n = int(sys.stdin.readline())
dp = list([0]*(n+1))

for i in range(1,n+1):
    j = 0
    dp[i] = i
    while j*j <= i:
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
        j += 1
print(dp[n])