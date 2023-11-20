import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
  a, b = map(int, input().split())
  print('Case #%d:' %(i+1), str(a+b))