# 40분
from itertools import product


def solution(users, emoticons):
    answer = []

    # 1순위 목표: 임티플러스 2순위: 순수판매액
    # 완전탐색
    discountRate = [10, 20, 30, 40]  # 0.1 0.2 0.3 0.4 로 썼다가 헤맸다 (단위가 달라서)

    res = []
    for rates in product(discountRate, repeat=len(emoticons)):

        plus = 0
        buy = 0
        for rate, money in users:
            ubuy = 0
            for i in range(
                    len(rates)):  # rantge(rates) 로 썼다가 엄청 헤맸다. #TypeError: 'tuple' object cannot be interpreted as an integer
                if rate <= rates[i]:
                    ubuy += emoticons[i] * (100 - rates[i]) // 100  # rate가 아닌 rates[i]를 넣어야 하는데.
            if ubuy >= money:
                plus += 1
            else:
                buy += ubuy
        res.append([plus, buy])

    res.sort(reverse=True)
    return res[0]