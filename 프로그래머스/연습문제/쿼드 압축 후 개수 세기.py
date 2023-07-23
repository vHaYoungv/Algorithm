[내 풀이]
cnt0 = 0
cnt1 = 0

def divide(arr):
    n = len(arr) // 2
    A = [arr[i][j] for i in range(n) for j in range(n)]
    B = [arr[i][j] for i in range(n) for j in range(n, 2 * n)]
    C = [arr[i][j] for i in range(n, 2 * n) for j in range(n)]
    D = [arr[i][j] for i in range(n, 2 * n) for j in range(n, 2 * n)]

    return [A, B, C, D]


def check(arr):
    global cnt0
    global cnt1

    arrSet = set()
    for x in arr:
        arrSet = arrSet | set(x)
    if len(arrSet) == 1:
        if list(arrSet)[0] == 0:
            cnt0 += 1
        elif list(arrSet)[0] == 1:
            cnt1 += 1
        return

    temp = []
    for x in divide(arr):
        Xset = set(x)
        if len(Xset) == 1:
            if list(Xset)[0] == 0:
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            n = int(len(x) ** (1 / 2))
            temp.append([list(x)[i * n:i * n + n] for i in range(n)])
    for x in temp:
        check(x)


def solution(arr):
    check(arr)
    return [cnt0, cnt1]
[참고 풀이]
# 다른 것을 찾았을 때! 그 때 나눠야 한다.
# 그래서 첫 값 first를 구하고 다른 값을 찾았을 때 나머지는 보지도 않고 바로 나누는 단계로 넘어가는 게 핵심이다.
def solution(arr):
    answer = [0, 0]

    def check(size, x, y): # def 안에 def 로 구성하면 global 변수를 쓰지 않고 간단하게 표현할 수 있다.
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer