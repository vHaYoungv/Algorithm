# [내 풀이]
# - 도착만 체크하는 것이 아니라 경로가 중요하므로 bfs가 아닌 dfs를 사용해야 한다.
# - 순서대로 방문을 체크하는 방법이 핵심이었던 문제. 순서대로 방문을 하지 못한 경우, 그 이후의 경로탐색을 중단해야 한다(return 이 아니라 continue....).
# * 순서대로 방문을 하지 못한 것 :
# 방문 리스트 안의 값인데 현재 당장 방문해야 되는 노드가 아닌 경우이다.
# 이 경우 순서가 꼬였다고 판단한다.
#
#
# - 흔한 유형인 dfs인데도... 1시간이 넘게 걸렸다. 한 문제에서 3번의 실수를 해버렸다.
# 1.  n이 아닌 m으로 초기 테이블 생성해버린 것
# 2. dfs 탐색 중단을 continue 가 아닌 return 으로 해버린 것
# 3. 디버깅 과정에서 값을 하드코딩해뒀던 것을 깜박하고 지우지 않은 것. 이런 건 방지를 위해서 ### 등으로 표시를 해두자.

import sys

n, m = map(int, sys.stdin.readline().split())
mtx = []
for i in range(n):
  mtx.append(list(map(int, sys.stdin.readline().split())))
todo = []
for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  todo.append([x-1, y-1])

visited = [[0]*n for _ in range(n)]

def dfs(lst, k):
  global cnt
  if k == m:
    cnt += 1
  else:
    x, y = lst
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] == 0 and mtx[nx][ny]==0:
          if [nx,ny] in todo and [nx,ny] != todo[k]:
            continue
          visited[nx][ny] = 1
          if [nx, ny] == todo[k]:
            dfs([nx,ny], k+1)
          else:
            dfs([nx,ny], k)
          visited[nx][ny] = 0

# 초기값
start = todo[0]
visited[start[0]][start[1]] = 1
cnt = 0

# 상수
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dfs(start, 1)
print(cnt)