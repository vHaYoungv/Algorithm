# 내 풀이
# 글자 수 순으로 정렬한 뒤, 이전의 결과와 중복 되지 않은 값이 그 순서에서 얻어야 하는 값이라는 아이디어
def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}') #문자열에서 리스트로?
    lst = s.split('},{')
    lst.sort(key=lambda x:len(x))
    for lst in [list(map(int, x.split(','))) for x in lst]:
        s = set(lst)
        answer.append(list(s-set(answer))[0])
    return answer

# 참고풀이
# 복잡하게 주어진 문자열에서 숫자 값만 빼는 것: re.findall('\d+', s) 활용하기
# Counter로 여러 번 세진 것이 가장 처음부터 있던 값 이라는 아이디어.
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
