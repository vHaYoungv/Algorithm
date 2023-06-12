# 내 풀이
def solution(progresses, speeds):
    time = []
    for i, x in enumerate(progresses):
        time.append((100 - x) // speeds[i] + (((100 - x) % speeds[i]) and 1))

    i = 0
    temp = []
    ret = []
    for x in time:
        if temp == []:
            temp.append(x)
        if temp[-1] < x:
            ret.append(i)
            i = 0
            temp.append(x)
        i += 1
    return ret + [i]

# 참고 풀이
# zip을 이용해서, p와 s를 간단하게 표현.
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]