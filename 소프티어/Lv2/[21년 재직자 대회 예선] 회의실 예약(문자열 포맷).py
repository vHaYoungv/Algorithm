# 단순 구현 문제, 문자열 포맷
# 연속된 0 구간 반환하는 것 더 간결하게 표현할 수 있는 방법은 없을까?
#
# 중요 포인트
# 리스트의 중간 값을 이렇게 바꿔치기 할 수 있다.
# rooms[room][s:e] = [1]*(e-s)
# 딕셔너리 키 기준 정렬 : 우선 sorted() 한 후, 딕셔너리가 리스트로 정렬되어 반환된 것을 다시 딕셔너리로
# print('{0:02d}'.format(s)+'-'+'{0:02d}'.format(e)) : 숫자 자릿수 달라질 때 0채워 반환하기

# 입력
n, m = map(int, input().split())
rooms = dict()
for i in range(n):
    rooms[input()] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(m):
    room, s, e = input().split()
    s, e = int(s) - 9, int(e) - 9
    for j in range(s, e):
        rooms[room][s:e] = [1] * (e - s)  # 이렇게 중간 값 바꿔치기 할 수 있다

# 딕셔너리 키 기준 정렬 : 리스트로 정렬된 것을 다시 딕셔너리로
rooms = dict(sorted(rooms.items()))

# 출력
for k, v in rooms.items():
    print('Room %s:' % k)
    if 0 not in v:
        print('Not available')
    else:
        i = 0
        s = 0
        e = 0
        temp = []
        while True:
            while i < 9 and v[i] != 0:
                i += 1
            if i == 9:
                break
            s = i
            while i < 9 and v[i] != 1:
                i += 1
            e = i
            temp.append((s + 9, e + 9))
            if i == 9:
                break

        print('%d available:' % len(temp))
        for s, e in temp:
            print('{0:02d}'.format(s) + '-' + '{0:02d}'.format(e))
    if k != list(rooms.keys())[-1]:
        print('-----')