# 내 풀이
# 똑같은 풀이인데 dp[i]에 값을 넣을 때 미리 나머지(10000007)을 계산한 후 넣은 것과 마지막에 %계산해 준 거랑 시간 차이가 엄청 심했다.
# 큰 숫자끼리 연산하는 게 훨씬 시간이 오래 걸리는 듯 하다. 그렇기 때문에 미리 나머지 계산을 해서 값을 저장 후 연산이 되도록 하자.
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 2
    for i in range(2,n):
        dp[i] = dp[i-2]+dp[i-1]

    return dp[n-1]%1000000007

# 내 풀이2
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 2
    for i in range(2,n):
        dp[i] = (dp[i-2]+dp[i-1])%1000000007

    return dp[n-1]
