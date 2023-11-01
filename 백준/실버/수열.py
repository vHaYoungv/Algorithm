from collections import deque
n, k = map(int, input().split())
data = list(map(int, input().split()))

res = (-100)*k #이거 때문에 몇 분 걸린걸까 .. ㅠㅠ
dq = deque()
now = sum(data[:k-1])
for i in range(n):
    # 일단 추가
    dq.append(data[i])
    # 길이 k이면 now 갱신, now값이 res보다 크면 res 갱신
    if len(dq) == k:
        now += data[i]
        if now > res: res = now
        now -= dq.popleft()
print(res)