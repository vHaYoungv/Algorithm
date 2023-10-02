# 7:33
# ak = ak-1 + a1
# ak = ak/N * aN
# ak = ak*N / aN
# ak = ak+1 - a1
def solution(N, number):
    # dfs...
    end = max(N * 11 + 1, number + 1)

    def dfs(k):

        # 업데이트가 일어나면 그 값에 대해 또 다시 체크
        if end > k + 1 >= 1 and dp[k + 1] > dp[k] + dp[1]:
            dp[k + 1] = dp[k] + dp[1]
            dfs(k + 1)
        if end > k - 1 >= 1 and dp[k - 1] > dp[k] + dp[1]:
            dp[k - 1] = dp[k] + dp[1]
            dfs(k - 1)
        if end > k + N >= 1 and dp[k + N] > dp[k] + dp[N]:
            dp[k + N] = dp[k] + dp[N]
            dfs(k + N)
        if end > k - N >= 1 and dp[k - N] > dp[k] + dp[N]:
            dp[k - N] = dp[k] + dp[N]
            dfs(k - N)
        if k % N == 0 and end >= k // N >= 1 and dp[k // N] > dp[k] + dp[N]:
            dp[k // N] = dp[k] + dp[N]
            dfs(k // N)
        if end > k * N >= 1 and dp[k * N] > dp[k] + dp[N]:
            dp[k * N] = dp[k] + dp[N]
            dfs(k * N)

    # aN 테이블
    dp = [9] * end
    # 초기값
    dp[1] = 2
    dp[N] = 1
    dp[N * 11] = 2
    dfs(1)
    print(dp)
    print(dp[N * 11])
    print(dp[(N * 11) // N])
    return -1 if dp[number] > 8 else dp[number]