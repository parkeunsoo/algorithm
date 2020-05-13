#2294
import sys
n,k = map(int,sys.stdin.readline().split())
coin = list()
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
dp = list([0]*(k+1))
for i in range(1,k+1):
    dp[i] = 100001
    for c in coin :
        if i >= c:
            if dp[i] > dp[i-c] + 1:
                dp[i] = dp[i-c] + 1
if dp[k] == 100001:
    print(-1)
else:     
    print(dp[k])
