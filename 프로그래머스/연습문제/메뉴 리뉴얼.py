# 내 풀이 : 성공, Counter, combinations 사용
from itertools import combinations as comb
from collections import Counter
def solution(orders, course):
    result = []
    for n in course:
        lst = []
        for order in orders:
            order = [x for x in order]
            for c in comb(order,n):
                s = ''.join(sorted(c))
                lst.append(s)
        dic = Counter(lst).most_common()
        if dic and dic[0][1] != 1:
            result += [d[0] for d in dic if d[1]==dic[0][1]]
    return sorted(result)

# 참고풀이 : 형태는 다르지만 나와 같은 로직의 풀이였다.
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]