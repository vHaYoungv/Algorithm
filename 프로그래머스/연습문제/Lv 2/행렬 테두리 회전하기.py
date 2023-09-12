[내 풀이]
from collections import deque


def toList(query):
    x1, y1, x2, y2 = query
    res = []
    for y in range(y1, y2 + 1):
        res.append((x1 - 1, y - 1))
    for x in range(x1 + 1, x2):
        res.append((x - 1, y2 - 1))
    for y in range(y2, y1 - 1, -1):
        res.append((x2 - 1, y - 1))
    for x in range(x2 - 1, x1, -1):
        res.append((x - 1, y1 - 1))
    return res


def solution(rows, columns, queries):
    # 초기값 세팅
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i - 1][j - 1] = ((i - 1) * columns + j)

    # 메인 루프
    answer = []
    for query in queries:
        positionList = toList(query)
        valueList = [matrix[i][j] for i, j in positionList]
        answer.append(min(valueList))
        positionList = deque(positionList)
        positionList.rotate(-1)
        for i in range(len(positionList)):
            x, y = positionList[i]
            matrix[x][y] = valueList[i]

    return answer

[참고 풀이]
- 스택 이용, 바로 n번 이전의 값.. 등: 스택 이용하기
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1

        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]

        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer