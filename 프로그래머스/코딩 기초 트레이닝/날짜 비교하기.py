[내 풀이]
def solution(date1, date2):
    return 1 if int(''.join(map(str, date1))) - int(''.join(map(str, date2)))<0 else 0

[참고 풀이]
- 리스트도 비교가 가능하구나
def solution(date1, date2):
    return int(date1 < date2)