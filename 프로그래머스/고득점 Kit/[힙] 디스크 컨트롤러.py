[내 풀이]
# 큐로 한쪽에서만 꺼낼 것이라면 굳이 deque()로 변환하지않고 정렬을 reverse=True로 한 후, pop() 을 이용하자
# 힙에는 '조건 맞는 것들 중' 정렬이 필요한 값들을 넣는다
import heapq as hq
def solution(jobs):
    jobsSorted = deque(sorted([[sT, yT] for yT, sT in jobs], key=lambda x:(x[1],x[0])))
    cT = 0
    tT = 0
    Q = []
    hq.heappush(Q, jobsSorted.popleft())
    while Q:
        sT, yT = hq.heappop(Q)
        cT = max(yT+sT, cT+sT) # 작업 완료 시간
        tT += cT - yT
        while jobsSorted and jobsSorted[0][1] <= cT:
            hq.heappush(Q, jobsSorted.popleft())
        if jobsSorted and not Q:
            hq.heappush(Q, jobsSorted.popleft())
    return tT//len(jobs)

[참고 풀이]
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)