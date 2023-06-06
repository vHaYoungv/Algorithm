# 내 풀이
# 최초 테스트 케이스는 통과했지만 [454, 45] 같은 경우는 통과하지 못해서 실패했다. 검색해서 확인해보니 *3을 곱해서 이런 케이스를 걸러내는 작업을 한다.
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# 참고 풀이
# int 인 채로 놔두지 않고, str로 변환한 후에 작업을 시작한다: 문자열 비교와 정수 비교의 대소 비교 방법 차이가 있기 때문이다.
# 따라서 정렬 결과도 다른 결과가 나오게 된다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 참고 풀이2
# a와 b가 int라면 당연히 같겠지만, a와 b가 str일 때를 고려한 설계
# key = functools.cmp_to_key(comparator) 숙지
# comparator 의 return 값이 양수이면 a,b로 정렬 음수이면 b,a로 정렬, 0이면 바뀌지 않음
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer