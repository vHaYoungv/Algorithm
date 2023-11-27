# 6:00 ~ 6:27
# 6:27 ~ 7:13 # 반례 생각하느라 ...
# 반례:
# 원래 알고리즘 대로라면, 가장 첫 로봇 부터 값이 결정 되어야 한다.
# 그런데 만약 내가 풀이한대로 하면, dq에 값이 다 차기 전에는, i번째에 값이 결정되어야 했던 것들이
# i보다 큰 위치에서 값이 결정되어 버린다. 이렇게 되면 값이 결정되는 순서가 뒤바뀌는 경우가 생길 수 있다.
# 기본적으로 로봇으로부터 가장 먼 왼쪽의 물품을 가져와야 알고리즘이 정상적으로 돌아가는데,
# i번째에 결정되어야 했던 것들이 보류 된 채 이후의 값들이 결정되는 사이에 순서가 바뀌어버리는 것이다.
import sys
from collections import deque
# 입력
n, k = map(int, input().split())
data = list(input())

idxdq = deque()
typedq = deque()
check = [0]*n
cnt = 0
for i,x in enumerate(data):
  if x=='P':
    if 'H' in typedq and check[idxdq[typedq.index('H')]]==0:
      check[idxdq[typedq.index('H')]] = 1
      check[i] = 1
      cnt += 1
  if x=='H':
    if 'P' in typedq and check[idxdq[typedq.index('P')]]==0:
      check[idxdq[typedq.index('P')]] = 1
      check[i] = 1
      cnt += 1
  if len(idxdq) == k:
    idxdq.popleft()
    typedq.popleft()
  idxdq.append(i)
  typedq.append(x)
print(cnt+1)