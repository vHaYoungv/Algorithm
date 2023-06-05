# 내 풀이
# 최초 테스트 케이스는 통과했지만 [454, 45] 같은 경우는 통과하지 못해서 실패했다. 검색해서 확인해보니 *3을 곱해서 이런 케이스를 걸러내는 작업을 한다.
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# 참고풀이
# int 인 채로 놔두지 않고, str로 변환한 후에 작업을 시작한다: 문자열 비교와 정수 비교의 비교 방법 차이가 있기 때문이다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))