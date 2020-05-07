import sys
N = int(sys.stdin.readline())
f = list([0]*N)
g = list([0]*N)


for i in range(N):
    f[i] = int(sys.stdin.readline())

f.sort(reverse=True)

answer = 0
for i in range(N):
    if answer < f[i]*(i+1):
        answer = f[i]*(i+1)

print(answer)