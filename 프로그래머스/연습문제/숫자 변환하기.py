# 내 풀이
# DFS로 풀면 최악의 경우를 끝까지 확인하기 때문에 시간초과가 날 수 있다. (그래서 최악의 경우를 끊어주는 경우 결과가 제대로 도출됐던 것 )
# 무조건 BFS로 풀었어야 했다
minCnt = 0
target = 0
step = 0
flag = False


def dfs(cnt, y):
    global minCnt
    global target
    global step
    global flag
    if y < target:
        return
    if y == target:
        minCnt = min(minCnt, cnt)
        flag = True
        return
    if cnt == minCnt:
        return
    else:
        if y % 3 == 0:
            dfs(cnt + 1, y // 3)
        if y % 2 == 0:
            dfs(cnt + 1, y // 2)
        if step != 0:
            dfs(cnt + 1, y - step)


def solution(x, y, n):
    global target
    target = x
    global minCnt
    minCnt = y
    global step
    step = n
    global flag
    flag = False

    if x == y: return 0

    dfs(0, y)

    return -1 if flag == False else minCnt
# 참고풀이
