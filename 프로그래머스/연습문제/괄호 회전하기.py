[내 풀이]
# 내 풀이가 오류가 발생할 경우 바로 False를 리턴해서 더 빠르긴 할 듯 하다.
from collections import deque
def check(s):
    stk = []
    for x in s:
        if x in ['(', '{', '[']:
            stk.append(x)
        else:
            if len(stk) == 0:
                return False
            if x == ')':
                if stk.pop() != '(':
                    return False
            if x == '}':
                if stk.pop() != '{':
                    return False
            if x == ']':
                if stk.pop() != '[':
                    return False
    if stk == []:
        return True

def solution(s):
    s = deque(s)
    ans = 0
    for i in range(len(s)):
        if check(''.join(s)):
            ans += 1
        s.rotate(-1)
    return ans

[참고 풀이]
# is_valid() 네이밍 센스
def is_valid(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch==')': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '{':
            if ch=='}': stack.pop()
            else: stack.append(ch)
        elif stack[-1] == '[':
            if ch==']': stack.pop()
            else: stack.append(ch)

    return False if stack else True

# s[i:]+s[:i]가 s.rotate(-1)랑 같은 의미를 갖는구나.
def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:]+s[:i])
    return answer