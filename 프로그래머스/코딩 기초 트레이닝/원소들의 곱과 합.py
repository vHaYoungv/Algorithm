# 모든 원소들의 곱은 함수가 없기 때문에 직접 구해야 한다. eval( )이용
# 다른 사람은 m = eval( )을 이용해서 문자열 수식을 만든 다음에 계산했다. ** 문자열 수식을 만들어 계산하는 방법!

def solution(num_list):
    gob = 1
    for x in num_list:
        gob = gob*x
    hob = sum(num_list)
    return 1 if gob < hob**2 else 0

def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0