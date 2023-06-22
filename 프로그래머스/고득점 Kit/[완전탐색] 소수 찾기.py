[내 풀이]
#문자열 => 리스트 : [n for n in numbers]
#숫자로 변환 : [int(("").join(p)) for p in per]
#근데 이렇게 하면 이미 소수 판별한것까지 다시 확인하는 거 아닌가?

from itertools import permutations

def solution(numbers):
    answer = []
    nums = [n for n in numbers]                   # numbers를 하나씩 자른 것
    per = []
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환

    for n in new_nums:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer))                       # set을 통해 중복 제거 후 반환


# Object of type set is not JSON serializable: set 자료형을 return 하려고 하니까 오류 발생
selected_numbers = set()


def dfs(l, res, numbers):
    global selected_numbers

    if len(numbers) == 0:
        selected_numbers.add(res)
    else:
        # 같은 수가 여러 개 있을 수도 있으니, 한 번만 계산하기 위해 걸러내는 과정
        temp = set(numbers)

        for x in temp:
            numbers.remove(x)
            dfs(l + 1, res + x, numbers)
            dfs(l + 1, res, numbers)
            numbers.append(x)


def isPrime(n):
    ch = [0] * (n + 1)
    prime = set()
    for i in range(2, n + 1):
        if ch[i] == 0:
            prime.add(i)
            for j in range(2 * i, n + 1, i):
                ch[j] = 1

    return list(prime)


def solution(numbers):
    global selected_numbers
    length = len(numbers)

    # remove를 사용하기 위해서, number를 리스트로 바꾸어주기
    numbers = [x for x in numbers]

    dfs(0, "", numbers)
    selected_numbers = set(map(int, selected_numbers - {''}))
    answer = selected_numbers & set(isPrime(max(selected_numbers)))

    return len(answer)

[참고 풀이]
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)