# 간단한 문자열 출력 문제
m, n, k = map(int,input().split())
key = ''.join(input().split())
ipt = ''.join(input().split())

if key in ipt:
  print('secret')
else:
  print('normal')