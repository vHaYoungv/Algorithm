# 내 풀이
# dic 이랑 counter 이랑 == 비교 할 수 있는 줄 모르고, counter로 변환 후 - 연산을 사용하려고 돌아간 점이 아쉬운 점
from collections import Counter
def solution(want, number, discount):
    wants = []
    for w, n in zip(want, number):
        wants += [w]*n
    w_counter = Counter(wants)

    cnt = 0
    for i in range(len(discount)-sum(number)+1):
        counter = Counter(discount[i:i+sum(number)])
        if not w_counter-counter:
            cnt += 1
    return cnt

# 참고풀이
# dic 이랑 counter이랑 ==비교 가능하다. counter는 dic을 확장한 것이기 때문이다.
from collections import Counter
def solution(want, number, discount):
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    cnt = 0
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): #dic 이랑 counter이랑 같다 체크할 수 있구나.
            cnt += 1
    return cnt