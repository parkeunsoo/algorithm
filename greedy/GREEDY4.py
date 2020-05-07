import sys
M = list(sys.stdin.readline())
M.pop(-1)
N = len(M)
M.sort(reverse=True)


def sol(M):
    SUM = 0 
    for i in M:
        SUM += int(i)
    if SUM % 3 == 0 and '0' in M:
        return ''.join(M)
    else:
        return -1
print(sol(M))