#11055
import sys
n = int(sys.stdin.readline())
v = list(map(int,sys.stdin.readline().split()))
dp = list([0]*n)

for i in range(n):
    row = list([0])
    for j in range(0,i):
        if v[j] < v[i]:
            row.append(dp[j])
    dp[i] = max(row) + v[i]
print(max(dp))

