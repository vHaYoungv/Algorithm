# 내 풀이
#무의식적으로 힙이 정렬된 리스트랑 같다고 생각했다.
#힙은 최소값만 보장하지, 나머지 값들은 오름차순이 아니라는 것을 주의해야한다.
#파이썬에서는 평범한 리스트에 heapq 함수를 사용하는 것일 뿐이다. 따라서 heappush를 한다고 힙이 되는 것은 아니다.
#일반 리스트를 힙 구조로 바꾸고 싶다면 O(n)이 걸리고 .heapify() 함수를 이용하면 된다. remove후에 꼭 다시 heapify()해주어야 한다.
import heapq as hq
def solution(operations):
    operations = [x.split() for x in operations]
    answer = []
    for op, x in operations:
        if op == "I":
            hq.heappush(answer, int(x))
        elif op == "D":
            if answer:
                if x=="-1":
                    hq.heappop(answer)
                else:
                    answer.remove(max(answer))
                    hq.heapify(answer) #꼭 heapify 다시 해주어야 한다.
    return [max(answer), answer[0]] if answer else [0, 0]