[내 풀이]
- 풀이 방향이 떠오르지 않았다.

[참고 풀이]
- 문자열을 set함수에 넣으면 구성 문자열들의 종류를 얻을 수 있구나. !!
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]