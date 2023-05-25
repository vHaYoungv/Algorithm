[내 풀이]
def solution(myString, pat):
    replaced = ""
    for x in myString:
        if x == "A":
            replaced += "B"
        else:
            replaced += "A"

    return int(pat in replaced)


[참고 풀이]
- 임시 변수인 C를 도입해서 두 번 바뀌게 되는 현상을 방지 (replace만 사용)
- myString 보다 pat이 더 짧기 때문에 myString 보다 pat을 replace 해서 체크 하는 것이 더 효율적일 수도 있다는 의견(문제의 취지와는 다르지만, 결과는 같다)
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))

