# 내 풀이
# 일부 실패
def solution(dirs):
    answer = 0
    moves = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visited = dict()
    x, y = 0, 0
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x+dx, y+dy
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        visited[(x,y,nx,ny)] = visited.get((x,y,nx,ny), 0) + 1
        x, y = nx, ny
    return len(visited.keys())

# 내 풀이2
def solution(dirs):
    answer = 0
    moves = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    visited = dict() #집합으로 표현했으면 add 만으로 중복 처리가 된다.
    x, y = 0, 0
    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x+dx, y+dy
        if nx<-5 or nx>5 or ny<-5 or ny>5: # if a<=x<=b and c<=y<=d 로 표현하는 게 더 깔끔했다.
            continue
        visited[(x,y,nx,ny)] = visited.get((x,y,nx,ny), 0) + 1
        x, y = nx, ny
    jungbok = 0
    for key in visited.keys():
        a, b, c, d = key
        if (c, d, a, b) in visited.keys():
            jungbok += 0.5
    return len(visited.keys()) - jungbok

# 참고 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2