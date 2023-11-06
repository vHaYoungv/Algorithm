# 7:23~7:46 실패
# 7:46~7:56 성공: 더 멀리 설치하려고 하다가, 설치 못하는 예외 처리
def solution(n, stations, w):
    s = 1
    cnt = 0
    for x in stations:
        for y in range(s+w, x, 2*w+1):
            print(y)
            cnt += 1
        s = x+w+1
    for y in range(s+w, n+w+1, 2*w+1):
        print(y)
        cnt += 1
    return cnt

