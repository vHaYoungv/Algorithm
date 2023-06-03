# 내 풀이
- mul = 1부터 for 문을 한 줄로 표현할 수 있다.
from collections import Counter
def solution(clothes):
    counter = Counter(map(lambda x:x[1],clothes))
    mul = 1
    for value in counter.values():
        mul *= (value+1)
    return mul - 1

# 참고풀이
- reduce(집계 함수, 순회 가능한 데이터, [초기값]) /from collections import reduce
- x는 초기값, y는 리스트에서 처음 값 부터 하나씩 계산되는 값
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer