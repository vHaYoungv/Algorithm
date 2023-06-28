[내 풀이]
def tenToN(x, n):
    nums = {k:v for k, v in zip(range(0,17), ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])}
    str = ''
    while x>=n:
        str += nums[x%n]
        x = x//n
    str += nums[x%n]
    return str[::-1]

def solution(n, t, m, p):
    num_list = []
    num = 0
    while len(num_list)<t*m:
        for x in tenToN(num, n):
            num_list.append(x)
        num += 1

    return ''.join(num_list[p-1::m][:t])

[내 풀이]
def tenToN(x, n):
    nums = {k:v for k, v in zip(range(0,17), ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])}
    str = ''
    while x>=n:
        str += nums[x%n]
        x = x//n
    str += nums[x%n]
    return str[::-1]

def solution(n, t, m, p):
    numbers = '' #굳이 리스트로 값을 받을 필요가 없었다. 리턴 값도 문자열이고, 슬라이싱 이용할 수 있는 건 같기 때문이
    num = 0
    while len(numbers)<t*m:
        numbers+=tenToN(num, n)
        num += 1
    return numbers[p-1:t*m:m] #t*m까지 구하면 된다

[참고 풀이]
def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0" #나랑 다르게 문자열에 데이터를 쌓아 반환. 이게 더 효율적이었다.
    for number in range(1, t*m):
        temp = [] #생각보다 진법 변환이 쉬워서 따로 함수 정의하지 않아도 되었을 수도 있겠다.
        while number > 0:
            temp.append(data[number%n])
            number //= n
        numbers += "".join(reversed(temp))

    return numbers[p-1:t*m:m]