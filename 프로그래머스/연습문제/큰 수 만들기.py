[내 풀이]
def solution(number, k):
    stk = []
    cnt = 0
    for i, n in enumerate(number):
        while stk and stk[-1]<n:
            stk.pop()
            cnt += 1
            if cnt == k:
                return ''.join(stk) + number[i:]
        stk.append(n)
    return ''.join(stk[:-(k-cnt)])

[참고 풀이]
# 나 처럼 제거한 숫자의 수 cnt 를 증가시키면서 cnt == k를 찾는 것이 아니라
# 변수 k를 그대로 사용하면서 조건이 만족할 때마다 k를 줄인 것이 코드 압축과 가독성에 좋은 효과를 줬던 듯하다.
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

[참고 풀이] #chat GPT
# number의 자릿수를 표현할 때: digit
def solution(number, k):
    stack = []

    for digit in number:
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 만약 k개의 수를 모두 제거하지 못했다면 남은 k개의 수를 뒤에서부터 제거
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)
