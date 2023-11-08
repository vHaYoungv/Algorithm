# 1:51 ~ 3:04
# n이 25니까 완전탐색
# A한번에 두번 갈 수 있는 거 처리해야함
# 이렇게 코드가 긴 거 맞나.....?

h, w = map(int, input().split())
mtx = [list(input()) for x in range(h)]

# 상수
# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = ['>', 'v', '<', '^']
# 길의 개수
length = sum([row.count('#') for row in mtx])

#
def dfs(x, y, m, k):
  global s
  global d
  global c
  global mins
  global mind
  global minc
  if k==length:
    z = 0
    tmpc = ''
    while z<len(c)-1:
      if c[z] == 'A' and c[z+1] == 'A':
        tmpc += 'A'
        z += 2
      else:
        tmpc += c[z]
        z += 1
    c = tmpc
    if len(c) < len(minc):
      mins = s
      minc = c
      mind = d
  for i in range(4):
    if k==1:
      d = i
      m = i
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and mtx[nx][ny]=='#':
      tmp = ''
      if -3 == i-m:
        tmp += 'R'
      if -2 <= i-m <0:
        tmp += 'L'*(m-i)
      if 0<= i-m <= 2:
        tmp += 'R'*(i-m)
      if 3 == i-m:
        tmp += 'L'
      tmp += 'A'
      c += tmp
      visited[nx][ny] = 1
      dfs(nx, ny, i, k+1)
      visited[nx][ny] = 0
      c = c[:-(len(tmp))]
mins = (0,0)
mind = 0
minc = 'A'*(10**6)
for i in range(h):
  for j in range(w):
    if mtx[i][j] == '#':
      visited = [[0]*w for _ in range(h)]
      visited[i][j] = 1
      s = (i,j)
      c = ''
      d = ''
      dfs(i, j, 0, 1)

print(mins[0]+1, mins[1]+1)
print(direction[mind])
print(minc)

