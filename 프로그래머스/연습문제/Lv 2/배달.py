[내 풀이]
from collections import deque


def solution(n, road, k):
    graph = [[] for _ in range(n + 1)]

    distance = [-1] * (n + 1)
    distance[1] = 0

    for x, y, l in road:
        graph[x].append((y, l))
        graph[y].append((x, l))

    dq = deque()
    dq.append((1, 0, [1]))
    while dq:
        x, d, lst = dq.popleft()
        for y, l in graph[x]:
            if y in lst:
                continue
            if distance[y] == -1 or distance[y] > d + l:
                if d + l <= k:
                    distance[y] = d + l
                    dq.append((y, d + l, lst + [y]))

    cnt = 0
    for i, x in enumerate(distance):
        if 0 <= x <= k:
            cnt += 1

    return cnt
[참고 풀이]
def solution(N, road, K):
    visited = [False] * (N + 1)
    costs = [float('inf')] * (N + 1)
    costs[1] = 0
    parents = [1]
    while (parents):
        parent = parents.pop(0)
        visited[parent] = True
        for a, b, cost in road:
            if (a == parent or b == parent):
                target = b if a == parent else a
                if costs[target] > costs[parent] + cost:
                    costs[target] = costs[parent] + cost
                    parents.append(target)

    return sum(1 for c in costs if c <= K)