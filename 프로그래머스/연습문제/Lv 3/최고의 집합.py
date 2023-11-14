# 1차: 6분, 성공
# 나는 n개의 몫을 원소로 갖는 먼저 리스트를 만들어두고, 나머지를 1단위로 분리해서 끝 부터 더해주는 방식으로 풀었다.
def solution(n, s):
    # -1 을 출력하는 조건
    if s//n == 0:
        return [-1]
    # 최고의 집합
    lst = [(s//n)]*n
    for i in range(s%n):
        lst[-1-i] += 1
    return lst

# 이 분은 아예 만들 때부터, 몫이 몇 개, 몫+1이 몇 개인지를 먼저 계산한 후 그 값만큼을 리스트에 넣어 반환했다. 이 분처럼 풀이하는 것이 정말 순수하게 n만큼만 돌기 때문에 속도가 빠를 것이다.
def bestSet(n, s):
    answer = []

    a = int(s / n)
    if a == 0:
        return [-1]

    b = s % n
    for i in range(n - b):
        answer.append(a)
    for i in range(b):
        answer.append(a + 1)

    return answer