# 특정 조건인 것들을 제거 하는 거 : Counter 활용해서 특정 조건을 뺄셈할 수 있었다.
def solution(participant, completion):
    for par in participant:
        if par not in completion:
            return par


# 해시 값으로 무슨 값이었는지 추적할 수 있다는 아이디어
def solution(participant, completion):
    dict = {}
    sumhash = 0

    for part in participant:
        dict[hash(part)] = part
        sumhash += hash(part)

    for comp in completion:
        sumhash -= hash(comp)

    return dict[sumhash]

# 참고 풀이
- from collections import Counter / Counter 활용하기
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]