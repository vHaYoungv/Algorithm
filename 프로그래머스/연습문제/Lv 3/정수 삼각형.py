# 1차 시도: 시간 초과
def solution(triangle):
    if len(triangle)==1:
        return triangle[0]
    lst = []
    for i, x in enumerate(triangle[0]):
        lst.append(max(solution(triangle[1:])[i]+x, solution(triangle[1:])[i+1]+x))
    return lst[0] if len(lst)==1 else lst

# 2차 시도: 통과
def solution(triangle):
    while triangle:
        if len(triangle) == 1:
            return triangle[0][0]
        tmp = triangle.pop()
        for i in range(len(tmp) - 1):
            triangle[-1][i] = triangle[-1][i] + max(tmp[i], tmp[i + 1])
