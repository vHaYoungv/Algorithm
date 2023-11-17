# 6:40 ~ 6:52 : 실패
from collections import deque
def solution(routes):
    routes.sort()
    routes = deque(routes)
    s, e = routes.popleft()
    cnt = 1
    while routes:
        ns, ne = routes.popleft()
        if e < ns:
            cnt += 1
            s, e = ns, ne
    return cnt

# 6:40 ~ 6:52 : 실패
# 6:52 ~ 6:57 : 수정 후 성공 (if ne<e 추가)
from collections import deque
def solution(routes):
    routes.sort()
    routes = deque(routes)
    s, e = routes.popleft()
    cnt = 1
    print(routes)
    while routes:
        ns, ne = routes.popleft()
        if ne < e:
            e = ne
        if e < ns:
            cnt += 1
            s, e = ns, ne
    return cnt