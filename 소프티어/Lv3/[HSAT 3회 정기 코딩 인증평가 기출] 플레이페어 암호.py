import sys

msg = input()
key = input()

# I와 J를 동일하게 보지만 편의상 J가 아예 주어지지 않음

# 주어진 키를 5X5 표로 변환
abc = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keytable = [['']*5 for _ in range(5)]


s = 0
for i in range(5):
  for j in range(5):
    while s<len(key) and key[s] not in abc:
      s += 1
    if s < len(key):
      keytable[i][j] = key[s]
      abc.remove(key[s])
    else:
      keytable[i][j] = abc.pop(0)

keytable2 = []
for row in keytable:
  for x in row:
    keytable2.append(x)

# 메세지를 두 글자씩 나눈다
# 중복 쌍 : 쌍을 파괴 : 'X'를 넣어 파괴
def divideMsg(msg):
  lst = []
  tmp = ''
  for i in range(len(msg)):
    if len(tmp) == 0:
      tmp += msg[i]
    elif len(tmp) == 1:
      if tmp[-1] == msg[i] and tmp[-1] =='X':
        lst.append(tmp+'Q')
        tmp = msg[i]
      elif tmp[-1] == msg[i] and tmp[-1] !='X':
        lst.append(tmp+'X')
        tmp = msg[i]
      else:
        lst.append(tmp+msg[i])
        tmp = ''
  if tmp:
    lst.append(tmp[0]+'X')
  return lst

# 표 반영해서 암호화
def encrypt(ab):
  a = ab[0]
  b = ab[1]
  aidx = keytable2.index(a)
  ai = aidx//5
  aj = aidx%5
  bidx = keytable2.index(b)
  bi = bidx//5
  bj = bidx%5
  if ai == bi:
    aj = (aj+1)%5
    bj = (bj+1)%5
  elif ai!=bi and aj==bj:
    ai = (ai+1)%5
    bi = (bi+1)%5
  else:
    aj, bj = bj, aj
  return keytable[ai][aj] + keytable[bi][bj]

# 실행
lst = divideMsg(msg)
res = ''
for x in lst:
  res += encrypt(x)
print(res)