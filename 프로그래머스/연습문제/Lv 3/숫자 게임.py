- 10분: 2개 실패
- 5분: "다른 팀의 점수를 늘리더라도, 내 팀의 점수도 같이 오르는 게 전략"인데, 동점일 경우도 포함해버리는 실수 수정
- 모든 A 값에 대해서, A값을 이기는 B의 값이 나올 때까지 while문을 돌린다.
from collections import deque
def solution(A, B):
    A.sort()
    B.sort()
    B = deque(B)
    cnt = 0
    for a in A:
        while B:
            b = B.popleft()
            if a<b:
                cnt += 1
                break
    return cnt

#다른 풀이
- 모든 B의 값에 대해서, A값을 이길 경우에만 다음 A값을 가져와 비교한다. 이게 더 문제를 그대로 표현한 풀이여서 좋은 것 같다.
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer