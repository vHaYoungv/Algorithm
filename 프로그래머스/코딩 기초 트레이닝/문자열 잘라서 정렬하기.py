[내 풀이]
- split('x'): x 기준으로 나누기 때문에 xx 같이 나란히 나오면, x, '', x 로 인식해서 ''도 추가된다.
def solution(myString):
    return sorted([x for x in myString.split('x') if x != ''])
