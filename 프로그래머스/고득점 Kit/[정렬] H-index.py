# 내 풀이
def solution(citations):
    answer = 0
    citations.sort()

    n = len(citations)
    for i in range(n):
        answer = max(answer, min(citations[i], n - i))

    return answer

# 참고풀이
# enumerate start 변수 지정할 수 있다. 1씩 증가하는 특정 변수로 활용하기 좋겠다.
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 참고풀이2
# l-i 는 점점 작아질 수 밖에 없기 때문에, 조건을 가장 먼저 통과한 값이 최댓값이 됨!
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
