number = int(input())
matrix = [[0]*number for _ in range(number)]
c = [[False]*number for _ in range(number)]
n = list()
team = 0
amount = 0

for i in range(number):
    value = list(map(int,input()))
    for j in range(number):
        matrix[i][j] = value[j]

def abc(number):
    row = 0
    col = 0
    global amount 
    global team
    while True:
        if row > (number-1) or col > (number-1):
            break
        if matrix[row][col] == 0 or c[row][col] == True:
            col += 1
            if col == number:
                row += 1
                col = 0
        else:
            n.append(dfs(row,col))
            team += 1
            amount = 0
            col += 1  
            if col == number:
                row += 1
                col = 0
    n.sort()
    print(team)
    for i in range(len(n)):
        print(n[i])

def dfs(row,col):
    global amount
    global number
    if c[row][col] == True:
        return
    amount += 1
    c[row][col] = True
    if row+1 < number and matrix[row+1][col] == 1:
        dfs(row+1,col)
    if col+1 < number and matrix[row][col+1] == 1:
        dfs(row,col+1)
    if row-1 >= 0 and matrix[row-1][col] == 1:
        dfs(row-1,col)
    if col-1 >= 0 and matrix[row][col-1] == 1:
        dfs(row,col-1)
    return amount

abc(number)
