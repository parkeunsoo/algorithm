equation = list(input().split('-'))
num = list()
for i in equation:
    cnt = 0
    gred = i.split('+')
    for j in gred:
        cnt += int(j)
    num.append(cnt)
answer = 0
for i in range(1,len(num)):
    answer -= num[i]

answer += num[0]
print(answer)