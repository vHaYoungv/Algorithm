# 순수 구현 문제
# 내 풀이
def solution(m, n, board):
    board = [list(row) for row in board]

    while True:
        temp = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '': continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    temp.update([(i,j), (i,j+1), (i+1,j), (i+1,j+1)])

        if not temp:
            break

        for i, j in temp:
            board[i][j] = ''

        temp = list(temp)
        temp.sort(key=lambda x:(x[1], -x[0]))

        for j in range(n):
            cnt = 0
            for i in range(m-1,-1,-1):
                if board[i][j] == '':
                    cnt += 1
                else:
                    if cnt == 0: continue
                    board[i+cnt][j] = board[i][j]
                    board[i][j] = ''

    return m*n-sum([1 for i in range(m) for j in range(n) if board[i][j] != ''])

# 참고풀이
def solution(m, n, board):
    x = board
    x2 =[]

    for i in x:
        x1 = []
        for i2 in i:
            x1.append(i2)
        x2.append(x1)

    point = 1
    while point != 0:
        list = []
        point = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '팡!':
                    list.append([i, j])
                    point += 1

        for i2 in list:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

        for i3 in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x2[i + 1][j] == '팡!':
                        x2[i + 1][j], x2[i][j] = x2[i][j], '팡!'

    cnt = 0
    for i in x2:
        cnt += i.count('팡!')
    return cnt