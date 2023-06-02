[내 풀이]
def solution(picture, k):
    answer = []
    for str in picture:
        tempstr = ""
        for x in str:
            tempstr += x*k
        answer += [tempstr]*k
    return answer

[참고 풀이]
- k번 반복시키는 것을 replace('.', '.'*k) 로 표현
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer