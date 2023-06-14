[내 풀이]
from collections import deque as dq
import heapq as hq

def solution(jobs):
    job_length = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = dq(jobs)

    total = 0  # 구하려는 값
    current_time = 0  # 행동 기준: 시간
    todo = []
    while jobs or todo:
        # 시간에 맞는 행동1: 그 시간에 시작 가능한 작업 큐에 넣기
        while jobs and jobs[0][0] <= current_time:
            hq.heappush(todo, (jobs[0][1], jobs[0][0]))
            jobs.popleft()
        # 시간에 맞는 행동2: 큐 중에서 제일 작업 시간 짧은 것 빼서 작업 / 비어있다면 대기(current_time+=1)
        if todo:
            a, b = hq.heappop(todo)
            current_time += a
            total += current_time - b
        else:
            current_time += 1

    return total // job_length