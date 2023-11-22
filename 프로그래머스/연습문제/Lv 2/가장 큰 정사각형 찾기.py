def solution(board):
    r = len(board)  #
    a = [[0] * (c := len(board[0])) for _ in range(r)]

    # a[i][j] 의 초깃값 설정
    for j in range(c):
        a[0][j] = board[0][j]
    for i in range(r):
        a[i][0] = board[i][0]

    # for문으로 a[i][j] 값 구하기
    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 1:
                a[i][j] = min(a[i - 1][j - 1], a[i - 1][j], a[i][j - 1]) + 1

    maxL = 0  # 초깃값 0
    for i in range(r):
        maxL = max(maxL, max(a[i]))

    return maxL ** 2