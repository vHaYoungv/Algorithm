# 내 풀이
# i번째 원소를 기준으로 나머지 값들을 전부 비교
def solution(prices):
    answer = []
    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            t += 1
            if prices[j]<prices[i]:
                break
        answer.append(t)
    return answer

# 참고풀이
# 값이 떨어지는 것이 발견 된 시점에서만 그 동안의 스택을 최근 부터 확인 후 결론 내기
# 스택 안의 값들은 모두 오름 차순인 것이 확실하기 때문에 가능한 것. 마지막 값만 확인하면 된다.
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

# 참고풀이 2
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer