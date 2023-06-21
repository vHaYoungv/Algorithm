[내 풀이]
# 굳이 sizes 다시 정의할 필요 없이, min, max만 활용하면 됐다.
def solution(sizes):
    sizes = [sorted(x) for x in sizes]
    garo = max([x[0] for x in sizes])
    sero = max([x[1] for x in sizes])
    return garo * sero

[참고 풀이]
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)