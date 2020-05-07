import sys
N = int(sys.stdin.readline())
v = list(map(int,sys.stdin.readline().split()))
dp = list([0]*N)
def sol(N):
    dp[0] = v[0]
    ans = v[0]
    su = dp[0]
    if N == 1 :
        return dp[0]
    for i in range(1,N):
        dp[i] = max(su+v[i],v[i])
        su = dp[i]
        ans = max(ans,dp[i])
    return ans
print(sol(N))
print(dp)