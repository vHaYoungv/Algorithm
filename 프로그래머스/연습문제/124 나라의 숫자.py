# 내 풀이(틀린풀이)
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

# 내 풀이2(정답풀이)
# 이진변환은 결국 1의 자리 결정난 후 그걸 토대로 앞의 n-1자리를 구하는 게 반복되는 방식이다. 이걸 진정으로 이해를 못했었다.
# 알고리즘 자체는 완전히 같지만 미리 n-=1 을 해줬으면 더 깔끔하게 표현 가능했다. (중복 연산 줄이기)
def solution(n):
    res = ''
    val = '124'
    while n>0:
        res = val[(n-1)%3] + res
        n = (n-1)//3
    return res

# 참고 풀이
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer