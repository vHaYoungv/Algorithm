# 내 풀이
def sosu(n):
    s = ''
    while n>0:
        s += str(n%3)
        n = n//3
    return s[::-1]

def solution(n):
    res = [int(x) for x in sosu(n)]
    for i, d in enumerate(sosu(n)):
        if d == '0':
            res[i] = 3
            res[i-1] = res[i-1]-1
    res = str(int(''.join(map(str,res)).replace('3','4')))
    return res
# 참고풀이
