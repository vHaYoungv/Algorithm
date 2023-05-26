[내 풀이]
- 이중 for문
def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            if i==j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)
    return answer

[참고 풀이]
- 리스트 컴프리헨션 안의 리스트 컴프리헨션
def solution(n):
    return [[int(i==j) for i in range(n)] for j in range(n)]

[참고 풀이2]
- 초기화 한 번만 하고, 특정 값만 수정하는 방식 (이게 더 빠르다.)
def solution(n):
    answer=[[0]*n for i in range(n)]
    for i in range(n): answer[i][i]=1
    return answer