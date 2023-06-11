[내 풀이]
# 더 깔끔하게 표현할 수 있는 방법 존재: 같은 cnt 변수를 쓰기 때문에 cnt = ~ if else ~ if ~ 와 같이 쓸 수 있었다.
# 변수 = 값1 if 조건1 else 값2 if 조건2 else 값3
def solution(s):
    cnt = 0
    for w in s:
        if cnt < 0:
            break
        cnt = cnt+1 if w=="(" else cnt-1 if w==")" else cnt
    return x==0


def solution(s):
    cnt = 0
    for x in s:
        cnt = cnt+1 if x=='(' else cnt-1
        if cnt < 0:
            break
    return cnt == 0

