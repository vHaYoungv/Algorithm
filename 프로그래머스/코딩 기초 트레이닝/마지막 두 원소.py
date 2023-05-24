# [내 풀이]
def solution(num_list):
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    return num_list

# [참고 풀이]
# 이게 더 지시문과 더 같은 의미의 코드. # l.append는 공통이고 어떤 값을 넣을지만 달라지는 것이니까!
# 최대한 지시문이 표현한 그대로 코드를 구현해보자.
# ( )안에도 함수가 그대로 들어갈 수 있다.
def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l