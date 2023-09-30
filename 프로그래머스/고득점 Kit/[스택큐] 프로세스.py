# 내 풀이
# if any(x<y for x, y in (zip([p]*len(pri_loc), [x[0] for x in pri_loc]))):
# if any(p < x[0] for x in pri_loc): 이렇게 표현해도 되는 것이었다.
from collections import deque
def solution(priorities, location):
    pri_loc = deque([(x ,i) for i, x in enumerate(priorities)])
    cnt = 0
    while pri_loc:
        p, l = pri_loc.popleft()
        if any(x<y for x, y in (zip([p]*len(pri_loc), [x[0] for x in pri_loc]))):
            pri_loc.append((p, l))
        else:
            cnt += 1
            if l == location:
                return cnt

# 참고풀이
# cur[1] < q[1] for q in queue 자체가 리스트로 취급되나보다.
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
