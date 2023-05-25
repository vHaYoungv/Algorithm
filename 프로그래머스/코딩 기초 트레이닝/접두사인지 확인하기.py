[내 풀이]
def solution(my_string, is_prefix):
    return int(my_string[:len(is_prefix)]==is_prefix)

[참고 풀이]
- startswith 라는 함수가 있다. *endswith 라는 함수도 있다.
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
