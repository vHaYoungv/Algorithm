# 5:08 ~ 5:32 # 24분
n = int(input())

# 점화식 문제
# an+1 = 4an -4bn + 1 (a1 = 4, b1 = 2)
# bn = 2*n-1 (b1 = 2)

dp_a = [4]
dp_b = [2]
for i in range(n):
  a = dp_a[-1]
  b = dp_b[-1]
  dp_a.append(4*a - 4*b +1)
  dp_b.append(2*b-1)

print(dp_a[n])