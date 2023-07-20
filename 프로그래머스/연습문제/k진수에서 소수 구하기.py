[내 풀이]
# 소수는 n<=1 일 때 false (n==1은 모자라다)
# 정규식 안 써도 간단하게 split('0') 쓰면 됐었다.
import re
def tenton(n, k):
    s = ""
    while n > 0:
        s += str(n % k)
        n //= k
    return s[::-1]

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):  # 범위 n으로 잡았더니 효율성에 걸렸다. 최소한으로 잡자!
        if n % i == 0:
            return False
    else:
        return True

def solution(n, k):
    p = re.compile('[1-9]+')
    s = tenton(n, k)
    lst = p.findall(s)
    return sum([1 for x in lst if isPrime(int(x))])

[참고 풀이]
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt