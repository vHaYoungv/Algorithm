[내 풀이]
# 최솟값이 계속 변화하고, 그것을 기준으로 알고리즘이 돌아가야함 => heapq 사용
# 런타임 에러: 아예 불가능한 경우 return -1 를 고려하지 않음

import heapq as hq


def solution(scoville, K):
    answer = 0

    scoville.sort()

    while len(scoville) >= 2 and scoville[0] < K:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        hq.heappush(scoville, a + 2 * b)
        answer += 1

    if scoville[0] < K:
        return -1

    return answer

[참고 풀이]
