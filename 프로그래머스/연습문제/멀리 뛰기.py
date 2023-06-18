[내 풀이]
# 피보나치 + dp
def solution(n):
    if n<3: # 이거 안해주면 오류 발생!
        return n
    table = [0]*(n)
    table[0] = 1
    table[1] = 2
    for i in range(2,n):
        table[i] = table[i-2]+table[i-1]
    return table[n-1]%1234567