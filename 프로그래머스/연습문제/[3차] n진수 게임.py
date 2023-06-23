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
    answer = ''

    num_list = []
    num = 0
    while len(num_list)<t*m:
        for x in tenToN(num, n):
            num_list.append(x)
        num += 1

    return ''.join(num_list[p-1::m][:t])

[참고 풀이]
def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    for number in range(1, t*m):
        temp = []
        while number > 0:
            temp.append(data[number%n])
            number //= n
        numbers += "".join(reversed(temp))

    return numbers[p-1:t*m:m]