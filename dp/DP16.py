#2293
import sys
n,k = map(int,sys.stdin.readline().split())
coin = list()
dp = list([0]*(k+1))
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
dp[0] = 1
for i in coin:
    for j in range(i,k+1):
        dp[j] += dp[j-i]
print(dp[k])
