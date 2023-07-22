[내 풀이]
- 시간 초과가 났던 풀이.
def solution(numbers):
    answer = []
    pX = 0
    pY = 0
    for i, x in enumerate(numbers):
        if pX < x:
            temp = numbers[i + 1:]
            for y in temp:
                if x < y:
                    pY = y
                    answer.append(y)
                    break
            else:
                answer.append(-1)

        else:
            pX = x
            answer.append(pY)

    return answer

[내 풀이2]
- 정석 풀이랑 점점 내 코드가 비슷해지는 것 같아 뿌듯하다...
def solution(numbers):
    answer = [-1] * (len(numbers))

    stk = [] #나는 값이 정해지기 직전에 변수 선언해 두는 게 나중에 이해하기 편한 것 같아 직전에 선언한다.
    for i in range(len(numbers) - 1):
        stk.append((i, numbers[i]))
        while stk and stk[-1][1] < numbers[i + 1]:
            answer[stk.pop()[0]] = numbers[i + 1]
    return answer

[참고 풀이]
1)
- 이 분은 값이 정해지는 시점을 i로 두고 풀이했다. 이게 더 깔끔한 것 같다.
- range가 깔끔하게 len(numbers)에 끝나 헷갈릴 부분이 없기 때문이다.
- 나는 값이 정해지고 나서 담기는 위치인 i를 기준으로 해서, i+1의 값을 미리 보고 올 수 밖에 없었다.
2)
- 스택에 i만 저장해도 된다. 어차피 numbers 리스트가 루프를 돌면서 변하는 것이 아니기 때문에 i만 저장해둬도 값이 필요하면 원래 리스트에서 numbers[i]를 꺼내오면 되기 때문이다.
def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
    return result
