# 내 풀이
# 원리 파악이 중요했던 문제
def solution(numbers):
    for i, num in enumerate(numbers):
        try:
            num = '0'+str(bin(num))[2:]
            f = num.rindex('0')
            if num[f+1]=='1':
                numbers[i] = int('0b'+num[:num.rindex('01')]+'10'+num[num.rindex('01')+2:], 2)
        except:
            numbers[i] = int('0b'+num[:num.rindex('0')]+'1'+num[num.rindex('0')+1:], 2)
    return numbers

# 참고풀이
# 비트 쉬프트 연산<< 2배 >>:1/2배
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer