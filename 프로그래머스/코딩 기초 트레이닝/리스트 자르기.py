[내 풀이]
- 이렇게 하면 마지막의 경우는 n번 조건문을 확인해야 해서, n이 커질 수록 이진 트리 방식으로 조건문을 나누는 게 좋다고 한다.
def solution(n, slicer, num_list):
    a,b,c = slicer
    if n==1:
        return num_list[:b+1]
    elif n==2:
        return num_list[a:]
    elif n==3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]

[참고 풀이]
- n에 따라 어떤 공식을 사용할 지 고르는 것을 리스트 안에 공식들을 넣어놓고 [n-1]인덱스를 찾아가도록 할 수 있구나.
def solution(n, slicer, num_list):
    a, b, c = slicer
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]
