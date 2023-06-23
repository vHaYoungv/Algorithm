[내 풀이]
# 3:39 - 3:58
def solution(msg):
    dic = [chr(i) for i in range(ord('A'), ord('A') + 26)]

    temp = ''
    answer = []
    for m in msg:
        if temp + m in dic:
            temp += m
            continue
        else:
            answer.append(dic.index(temp) + 1)
            dic.append(temp + m)
            temp = m
    answer.append(dic.index(temp) + 1)

    return answer

[참고 풀이]
#처음 정의할 땐 귀찮지만, d로 값 빼오는 게 이후 가독성이 훨씬 좋다. (dic.index(temp)와 비교됨)
#temp+=m과 동일한 원리지만, 한 글자 더 추가한다는 것이 더 명확하게 전달되기 때문에 이렇게 표현하는 게 가독성이 더 좋았을 듯 하다.
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))} #처음 정의할 땐 귀찮지만, d로 값 빼오는 게 이후 가독성이 훨씬 좋다. (dic.index(temp)와 비교됨)

    answer = []
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d: #temp+=m과 동일한 원리지만, 한 글자 더 추가한다는 것이 더 명확하게 전달되기 때문에 이렇게 표현하는 게 가독성이 더 좋았을 듯 하다.
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer