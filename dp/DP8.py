import sys
N = int(sys.stdin.readline())
wine = list([0]*(N+1))
dp = list([0]*(N+1))
for i in range(1,N+1):
    wine[i] = int(sys.stdin.readline())

def sol(N):
    dp[1] = wine[1]
    if N==1:
        return dp[1]
    dp[2] = wine[1]+wine[2]
    if N==2:
        return dp[2]
    dp[3] = max(wine[1]+wine[2],wine[2]+wine[3],wine[1]+wine[3])
    if N==3:
        return dp[3]
    dp[4] = max(wine[1]+wine[2]+wine[4],wine[1]+wine[3]+wine[4],wine[2]+wine[3])
    if N==4:
        return dp[4]
    for i in range(5,N+1):
        dp[i] = max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-4]+wine[i-2]+wine[i-1])
    return dp[N]

print(sol(N))
print(dp)