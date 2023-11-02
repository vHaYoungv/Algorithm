# str.find(찾을값) : 인덱스 리턴
# 스택...
str = input()
bomb = input()
n = len(bomb)

stk = []
for x in str:
    stk.append(x)
    if ''.join(stk[-n:]) == bomb:
        for i in range(n):
            stk.pop()

if ''.join(stk)=='':
    print("FRULA")
else:
    print(''.join(stk))