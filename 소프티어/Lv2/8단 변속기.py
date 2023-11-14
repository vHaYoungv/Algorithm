import sys
ipt = list(map(int, sys.stdin.readline().split(' ')))

ascList = [1, 2, 3, 4, 5, 6, 7, 8]
desList = ascList[::-1]

if ipt == ascList:
  print('ascending')
elif ipt == desList:
  print('descending')
else:
  print('mixed')