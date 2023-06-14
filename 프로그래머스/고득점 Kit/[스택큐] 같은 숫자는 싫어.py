# 내 풀이
def solution(arr):
    answer = []
    for x in arr:
        if answer == [] or answer[-1] != x:
            answer.append(x)
    return answer
# 참고 풀이
# 빈 배열일 가능성이 있는 경우 슬라이싱 활용
# answer[-1] 은 빈 배열일 때 오류가 나지만, answer[-1:]은 오류가 나지 않는다.
def solution(arr):
    answer = []
    for x in arr:
        if answer[-1:] == [x]: continue
        answer.append(x)
    return answer