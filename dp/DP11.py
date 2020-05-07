import sys
N = int(sys.stdin.readline())
v = list(map(int,sys.stdin.readline().split()))
dp = list([1]*N)
for n in range(0,N):
    row = list([0])
    for j in range(0,n):
        if v[j] < v[n]:
            row.append(dp[j])
    dp[n] = max(row)+1 # 자기보다 작은 값들의 dp중 가장 큰 값에 +1
    print("row:", row)

print(dp)
print(max(dp))
