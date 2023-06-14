[내 풀이]
def solution(s):
    stk = []
    for x in s:
        if x == '(':
            stk.append(x)
        else: 
            if stk == []:
                return False
            else:
                stk.pop()
    return True if len(stk)==0 else False

# 실제 stk에 무슨 값이 있나보다는, 개수가 중요하기 때문에 cnt를 기준으로 생각하는 게 효율적이다. 
# 더 깔끔하게 표현할 수 있는 방법 존재: 같은 cnt 변수를 쓰기 때문에 cnt = ~ if else ~ if ~ 와 같이 쓸 수 있었다. 
# 변수 = 값1 if 조건1 else 값2 if 조건2 else 값3 

[참고 풀이]
def solution(s):
    cnt = 0
    for x in s:
        cnt = cnt+1 if x=='(' else cnt-1 
        if cnt < 0:
            break
    return cnt == 0