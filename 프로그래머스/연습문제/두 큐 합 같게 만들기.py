# 내 풀이
# 가장 중요한 것: 변수에 내가 원하는 값이 제대로 들어가고 있는지 먼저 테스트하는 것.
# 이 부분을 빨리 캐치하지 못하면 로직을 제대로 짜고도 '왜 안나오지'만 반복하게 된다.
from collections import deque


def solution(q1, q2):
    #
    if (sum(q1) + sum(q2)) % 2 != 0:
        return -1
    if sum(q1) == sum(q2):
        return 0

    #
    n = len(q1)
    q1 = deque(q1)
    q2 = deque(q2)
    sum1 = sum(q1)
    sum2 = sum(q2)

    cnt = 0
    while sum1 != sum2:
        if cnt >= 4 * n:
            return -1
        if sum1 < sum2:
            v = q2.popleft()
            q1.append(v)
            sum1 += v
            sum2 -= v
        elif sum1 > sum2:
            v = q1.popleft()
            q2.append(v)
            sum1 -= v
            sum2 += v
        cnt += 1

    return cnt

# 참고풀이
