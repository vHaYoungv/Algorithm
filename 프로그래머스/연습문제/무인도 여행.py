# 내 풀이 (런타임 에러): 재귀 문제는 최대 깊이 제한 꼭 풀어주자. 파이썬은 최대 깊이가 1000이라 10^6까지 풀어주는 게 좋다.
food = 0
def solution(maps):
    global food
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        global food
        if not visited[x][y] and graph[x][y] != 'X':
            food += int(graph[x][y])
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx, ny)

    answer = []
    graph = [[x for x in m] for m in maps]
    n = len(graph)
    m = len(graph[0])
    visited = [[0 for x in m] for m in maps]

    # dfs
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            food = 0
            dfs(i, j)
            if food != 0:
                answer.append(food)
    return sorted(answer) or [-1]

# 내 풀이2 (성공)
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)
food = 0

def solution(maps):
    global food
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        global food
        if not visited[x][y] and graph[x][y] != 'X':
            food += int(graph[x][y])
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx, ny)

    answer = []
    graph = [[x for x in m] for m in maps]
    n = len(graph)
    m = len(graph[0])
    visited = [[0 for x in m] for m in maps]

    # dfs
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            food = 0
            dfs(i, j)
            if food != 0:
                answer.append(food)
    return sorted(answer) or [-1]
