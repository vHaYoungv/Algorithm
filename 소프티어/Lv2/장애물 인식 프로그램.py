# 1:00~ 1:21
# 제약 조건을 항상 맨 위에 주석으로 써놓는 습관
import sys

n = int(input())
mtx = []
for i in range(n):
    mtx.append(list(map(int, input())))

# 상수
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# dfs
def dfs(x, y):
    global block
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if mtx[nx][ny] == 1:
                mtx[nx][ny] = 0
                block += 1
                dfs(nx, ny)


# 전체 뼈대
cnt = 0
blockcnt = []
for a in range(n):
    for b in range(n):
        if mtx[a][b] == 1:
            block = 1
            mtx[a][b] = 0
            dfs(a, b)
            cnt += 1
            blockcnt.append(block)

blockcnt.sort()  ### 이 한 줄 때문에... 틀렸다!
print(len(blockcnt))
for x in blockcnt:
    print(x)