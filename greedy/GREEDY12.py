#1138
import sys
N = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
v = list([False]*N)

for i in range(N):
    a = p[i]
    j = 0
    while a != 0 :
        if v[j] == False:
            a -= 1
        j += 1
    while v[j] != False:
        j = j+1
    v[j] = i+1
for i in range(N):
    print(v[i], end=" ")

