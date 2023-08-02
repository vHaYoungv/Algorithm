# 내 풀이
# 얘는 실패뜬다.
def solution(land):
    dp = []
    for lan in land:
        if dp==[]:
            dp.append(lan)
        else:
            temp = dp[-1][:]
            for i in range(4):
                temp[i] = temp[i] + max(lan[:i]+lan[i+1:])
            dp.append(temp)
    return max(dp[-1])

# 참고풀이
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
