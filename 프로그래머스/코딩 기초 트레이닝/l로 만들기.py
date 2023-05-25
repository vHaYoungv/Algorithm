[내 풀이]
def solution(myString):
    return ''.join("l" if x<"l" else x for x in myString)

[참고 풀이]
- 문자열 translate(table), table = str.maketrans(문자열1, 문자열2) 사용
def solution(myString):
    return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

