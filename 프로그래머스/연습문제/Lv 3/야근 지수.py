# 1차: 11분, 통과
import heapq
def solution(n, works):
    works = list(map(lambda x:-x, works))
    heapq.heapify(works)
    while works and n>=1:
        now = heapq.heappop(works)
        if now >= 0:
            return 0
        heapq.heappush(works, now+1)
        n -= 1
    return sum([x**2 for x in works])