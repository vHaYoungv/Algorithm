[내 풀이]
- 완전탐색, dfs 활용
- global 변수 사용 없이 할 수 없을까?

import sys
sys.setrecursionlimit(10 ** 9)
minRes = 10 ** 9


def dfs(i, res, cnt):
    global minRes
    if res >= minRes:
        return
    if i == 0:
        minRes = res
        return
    else:
        b = i % 10
        dfs(i // 10, res + b, cnt + 1)
        dfs((i + 10 - b) // 10, res + (10 - b), cnt + 1)


def solution(storey):
    global minRes
    dfs(storey, 0, 0)
    return minRes

[대표 풀이]
- dfs에서 min 함수를 이용하여 재귀 돌리는 방법. 아래 트리 전체 중에서 최솟값을 얻어낼 수 있다.
- 나의 풀이와 완전히 같은 로직이지만, min 함수를 활용하느냐 하나로 minRes 라는 변수 없이도 코딩할 수 있었고, 더 직관적이면서 짧게 표현할 수 있었다.
- 단점이라면 정말 전체 경우의 수를 계산해야 할 것이다. 나 처럼 일정 이상이면 더 이상 계산 안한다든가 하는 방법을 추가 할 수 없다.

def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))