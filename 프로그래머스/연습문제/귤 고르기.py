[내 풀이]
from collections import Counter
def solution(k, tangerine):
    answer = 0
    box = 0
    counter = Counter(tangerine).most_common()
    for a, b in counter:
        box += b
        answer += 1
        if box >= k:
            return answer

[참고 풀이]
# tangerine.sort(key = lambda t: (-counter[t], t)) 를 통해서 개수 많은 순으로 정렬해 둠 => 그 박스에 어떤 과일이 몇 개씩 들어가는지 까지 값을 정리할 수 있다.
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))
