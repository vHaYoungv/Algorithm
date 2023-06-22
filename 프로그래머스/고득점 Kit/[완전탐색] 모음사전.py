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

[참고 풀이]
from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1