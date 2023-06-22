[내 풀이]
from collections import deque
def solution(n, wires):
    answer = -1
    minCnt = 101
    visited = [0]*n
    for i, x in enumerate(wires): #리스트에서 하나의 값 뺀 리스트 구하는 효율적인 방법? #참고 풀이에서는 슬라이싱
        temp = wires[:]
        temp.pop(i)
        cnt = 0
        visited = [0]*n
        graph = [[0]*n for _ in range(n)]
        for a, b in temp:
            graph[a-1][b-1] = 1
            graph[b-1][a-1] = 1
        Q = deque([temp[0][0]])
        while Q:
            k = Q.popleft()
            if not visited[k-1]:
                visited[k-1] = 1
                cnt += 1
                for j, x in enumerate(graph[k-1]):
                    if x == 1 and not visited[j]:
                        Q.append(j+1)
        minCnt = min(abs((cnt)-(n-cnt)),minCnt)
    return minCnt

[참고 풀이]
# s는 방문한 노드들
# 방문한 노드 들과 공통 노드가 있으면, update
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0]) # s는 방문한 노드들
        [s.update(v) for _ in sub for v in sub if set(v) & s] # 방문한 노드 들과 공통 노드가 있으면, update
        ans = min(ans, abs(2 * len(s) - n))
    return ans