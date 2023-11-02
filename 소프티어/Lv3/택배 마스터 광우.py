# 완전 탐색
import sys
from itertools import permutations

n, m, k = map(int, input().split())
rails = list(map(int, input().split()))

minV = m * k
for rail in permutations(rails, n):
    cnt = 0
    V = 0
    baguni = 0
    i = 0
    while cnt < k:
        if i == n:
            i = 0
        if baguni + rail[i] > m:
            V += baguni
            baguni = 0
            cnt += 1
            continue
        baguni += rail[i]
        i += 1
    if minV > V: minV = V
print(minV)

