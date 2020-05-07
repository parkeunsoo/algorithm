import sys
from itertools import combinations
sys.setrecursionlimit(100000)
sol = list()
while True:
    uinput = list(map(int,sys.stdin.readline().split()))
    if uinput[0] == 0:
        break
    T=uinput.pop(0)
    answer = list(combinations(uinput,6))
    sol.append(answer)

for row in sol:
    for value in row:
        for v in value:
            print(v,end=" ")
        print()
    print()