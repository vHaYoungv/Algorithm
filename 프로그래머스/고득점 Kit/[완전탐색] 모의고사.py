[내 풀이]
def solution(answers):
    score = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, x in enumerate(answers):
        if p1[i % 5] == x:
            score[0] += 1
        if p2[i % 8] == x:
            score[1] += 1
        if p3[i % 10] == x:
            score[2] += 1

    return [i + 1 for i, x in enumerate(score) if x == max(score)]

[참고 풀이]
# len(pattern) 으로 5, 8, 10을 상수가 아닌 동일한 값인 len(pattern)으로 표현할 수 있기 때문에, 이를 활용하여 간결하게 작성 가능
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

