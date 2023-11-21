# 15분
from collections import Counter


def solution(weights):
    answer = 0

    # 1:1, 1:2, 2:3, 3:4  관계인 개수 구하기

    # 딕셔너리를 이용한 풀이
    w_dict = Counter(weights)  # N = 10만
    for k, v in w_dict.items():  # N = 40만
        if v >= 2:
            answer += v * (v - 1) // 2
        for c in [2, 3 / 2, 4 / 3]:
            if k * c in w_dict:
                answer += v * w_dict[k * c]
    return answer