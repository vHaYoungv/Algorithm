[내 풀이]
# 처음에 가정을 잘못 했다.
minDistance = 10 ** 9


def outLine(rectangle):
    x1, y1, x2, y2 = rectangle
    outPoints = []
    for x in range(x1, x2 + 1):
        outPoints.append((x, y1))
    for x in range(x1, x2 + 1):
        outPoints.append((x, y2))
    for y in range(y1 + 1, y2):
        outPoints.append((x1, y))
    for y in range(y1 + 1, y2):
        outPoints.append((x2, y))
    return outPoints


def inside(rectangle):
    x1, y1, x2, y2 = rectangle
    insidePoints = []
    for i in range(x1 + 1, x2):
        for j in range(y1 + 1, y2):
            insidePoints.append((i, j))
    return insidePoints


def solution(rectangles, characterX, characterY, itemX, itemY):
    global minDistance

    def dfs(x, y, distance):
        print(x, y, distance)
        global minDistance
        if x == itemX and y == itemY and minDistance > distance:
            print(x, y, distance, 'end')
            minDistance = distance
            return
        visited[x][y] = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        res = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in outLines and not visited[nx][ny]:
                dfs(nx, ny, distance + 1)
                visited[nx][ny] = 0

    visited = [[0] * (52) for _ in range(52)]

    insides = []
    for rectangle in rectangles:
        insides += inside(rectangle)

    outLines = []
    for rectangle in rectangles:
        RoutLine = outLine(rectangle)

        for o in RoutLine:
            if o in insides:
                continue
            outLines.append(o)
    outLines = list(set(outLines))
    print(sorted(list(set(outLines))))
    dfs(characterX, characterY, 0)

    return minDistance