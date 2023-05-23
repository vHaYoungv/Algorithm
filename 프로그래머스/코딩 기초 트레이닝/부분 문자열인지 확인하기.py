# 내 풀이
def solution(my_string, target):
    return 1 if target in my_string else 0


# 참고 풀이 # int(True) = 1, int(False) = 0
def solution(my_string, target):
    return int(target in my_string)
