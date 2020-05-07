import sys
N, M = map(int,sys.stdin.readline().split())
package = list([0]*M)
indiv = list([0]*M)

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    package[i] = x
    indiv[i] = y

package.sort()
indiv.sort()
answer = 0
if package[0] < 6*indiv[0]:
    answer += N//6 * package[0]
    if package[0] < (N%6)*indiv[0]:
        answer += package[0]
    else:
        answer += (N%6)*indiv[0]
else:
    answer += N*indiv[0]

print(answer)