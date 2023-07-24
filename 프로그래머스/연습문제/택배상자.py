[내 풀이]
def solution(orders):
    answer = []

    belt = list(range(1, len(orders) + 1))
    stk = []
    i = 0

    for order in orders:
        if stk and stk[-1] == order:
            answer.append(stk.pop())
            continue
        while i < len(orders) and belt[i] != order:
            stk.append(belt[i])
            i += 1
        if i < len(orders) and belt[i] == order:
            answer.append(order)
            i += 1
            continue
        break

    return len(answer)


[참고 풀이]
# 간단하게 풀 수 있는 문제였다... 기준을 들어오는 택배 상자로 했으면 ㅠㅠ
def solution(order):
    stk = []
    i = 1
    idx = 0
    while i < len(order)+1:
        stk.append(i)
        while stk[-1] == order[idx]:
            idx += 1
            stk.pop()
            if len(stk) == 0:
                break
        i += 1


    return idx