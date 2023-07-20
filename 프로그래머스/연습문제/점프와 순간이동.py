[내 풀이]
# DP로 접근하려고 해서 시간 초과가 났었던 문제

[참고 풀이]
# n이 1억 단위인 것을 보고 O(logN) 을 떠올렸어야 한다.
# 복잡할 줄 알았지만, n /= 2 될 것이라는 것을 예측할 수 있었어야 했다.

def solution(n):
    cnt = 0
    while n>0:
        if n%2 == 0:
            n /= 2
        else:
            cnt += 1
            n = (n-1)//2
    return cnt