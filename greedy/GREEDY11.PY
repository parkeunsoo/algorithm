import sys
N = int(sys.stdin.readline())
v = list(map(int,sys.stdin.readline().split()))
a = list([0]*N)
sol = list()

for value in v:
    if a[value-1] == 0:
        a[value-1] = 1
    for i in range(value-1):
        if a[i] + 1 > a[value-1]:
            a[value-1] = a[i] + 1
print(max(a))


