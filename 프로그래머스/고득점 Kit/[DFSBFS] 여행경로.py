# 모든 도시를 방문할 수 없는 경우는 없다
# 주어진 항공권은 모두 사용해야 한다
# 이 두가지 조건덕에 stk에서 pop되는 게 무조건 answer 도착지 마지막 부분이라는 것을 확신 가능

from collections import defaultdict


def solution(tickets):
    answer = []
    t_dict = defaultdict(list)

    # {출발지:[도착지들]}
    for ticket in tickets:
        t_dict[ticket[0]].append(ticket[1])

    for key in t_dict.keys():
        t_dict[key].sort(reverse=True)

    stk = ['ICN']
    while stk:
        now = stk[-1]
        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(stk.pop())
        else:
            stk.append(t_dict[now].pop())
    return answer[::-1]