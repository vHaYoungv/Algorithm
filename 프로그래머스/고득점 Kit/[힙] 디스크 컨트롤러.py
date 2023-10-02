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

[내 풀이2]
# 3:07 ~ 4:00 // 오래 걸렸다... 11,17,20 빼고 실패
import heapq as hq


def solution(jobs):
    # 걸린 시간을 최소로 하려면, 당장 실행 가능한 프로그램들 중에서 제일 짧은 프로그램을 먼저 처리하면 된다.
    length = len(jobs)
    currentTime = jobs[0][0]
    totalTime = 0
    heap = []
    hq.heappush(heap, (jobs[0][1], jobs[0][0]))
    jobs.pop(0)
    while heap:
        # 힙에 넣어진 작업을 하나 수행
        pT, gT = hq.heappop(heap)

        # 현재 시간과 totalTime 다시 계산
        totalTime += pT + (currentTime - gT)
        currentTime += pT

        # 만약 힙이 비어있어서, 멈추게 되는 경우 다음 작업의 getTime 까지 이동
        if not heap and jobs and currentTime < jobs[0][0]:
            currentTime = jobs[0][0]

        # 현재 시간보다 더 이른 getTime을 가진 job들은 모두 힙에 넣기
        while jobs and jobs[0][0] <= currentTime:
            getTime, playTime = jobs.pop(0)
            hq.heappush(heap, (playTime, getTime))
    return (totalTime) // length

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