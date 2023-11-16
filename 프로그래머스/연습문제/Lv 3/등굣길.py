# 7분 : 런타임에러
def solution(m, n, puddles):
    answer = 0
    # n, m 순이다
    graph = [[0] * m for _ in range(n)]

    for j in range(m):
        graph[0][j] = 1

    for i in range(n):
        graph[i][0] = 1

    for i, j in puddles:
        graph[i][j] = -1

    # 둘 중 하나가 1인 경우 생각하기
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == -1:
                continue
            graph[i][j] = (0 if graph[i - 1][j] == -1 else graph[i - 1][j]) + (
                0 if graph[i][j - 1] == -1 else graph[i][j - 1])

    return graph[n - 1][m - 1]


# 7분 : 런타임에러
# 3분 : 실패
def solution(m, n, puddles):
    answer = 0
    # n, m 순이다
    graph = [[0] * m for _ in range(n)]

    for j in range(m):
        graph[0][j] = 1

    for i in range(n):
        graph[i][0] = 1

    for i, j in puddles:
        graph[j - 1][i - 1] = -1

    # 둘 중 하나가 1인 경우 생각하기
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == -1:
                continue
            graph[i][j] = (0 if graph[i - 1][j] == -1 else graph[i - 1][j]) + (
                0 if graph[i][j - 1] == -1 else graph[i][j - 1])

    for row in graph:
        print(row)

    return graph[n - 1][m - 1]


# 7분 : 런타임에러
# 3분 : 실패
# 2분 : 10000007로 나눈 나머지라니 ... 근데 이건 영향 없네
# 10분 : -1먼저 처리해야하는 구나
def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]

    for i, j in puddles:
        graph[j - 1][i - 1] = -1

    for j in range(m):
        if graph[0][j] == -1:
            break
        graph[0][j] = 1

    for i in range(n):
        if graph[i][0] == -1:
            break
        graph[i][0] = 1

    # 둘 중 하나가 1인 경우 생각하기
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == -1:
                continue
            graph[i][j] = (0 if graph[i - 1][j] == -1 else graph[i - 1][j]) + (
                0 if graph[i][j - 1] == -1 else graph[i][j - 1])

    for row in graph:
        print(row)

    return (graph[n - 1][m - 1]) % 1000000007