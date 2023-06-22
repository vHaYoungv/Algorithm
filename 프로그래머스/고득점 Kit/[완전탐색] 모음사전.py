[내 풀이]
dic = []
lst = ['', 'A', 'E', 'I', 'O', 'U']
def dfs (k, str):
    global dic
    if k==5:
        dic.append(str)
    else:
        for x in lst:
            dfs(k+1, str+x)

def solution(word):
    global dic
    dfs(0, '')
    dic = sorted(list(set(dic)))
    return dic.index(word)

[내 풀이2]
# 참고 풀이의 product 개념을 적용하여 직접 다시 풀어본 풀이
from itertools import product
def solution(word):
    dic = []
    lst = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for x in product(lst, repeat=i):
            dic.append(''.join(x))
    dic.sort()
    return dic.index(word)+1

[참고 풀이]
# product의 repeat변수를 이용하여 더 쉽게 풀이할 수 있다.
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1