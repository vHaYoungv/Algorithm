[내 풀이]
-시간 초과
def solution(topping):
    answer = 0
    for i in range(1, len(topping)):
        if len(set(topping[:i])) == len(set(topping[i:])):
            answer += 1
    return answer

[내 풀이2]
def solution(topping):
    topping2 = topping[::-1]

    Aset, Bset = set(), set()
    a, b = 0, 0
    Alist, Blist = [], []
    for i in range(len(topping) - 1):
        if topping[i] not in Aset:
            a += 1
            Aset.add(topping[i])
        Alist.append(a)
        if topping2[i] not in Bset:
            b += 1
            Bset.add(topping2[i])
        Blist.append(b)

    return sum([x == y for x, y in zip(Alist, Blist[::-1])])

[참고 풀이]
- Counter를 이용한 방법.
from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer