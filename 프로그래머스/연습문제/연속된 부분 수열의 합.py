# 내 풀이 (시간 초과) : sum(seq[s:e]) 때문에 불필요하게 리스트를 돌면서 부분합을 구하게 됨, 차이가 나는 원소 값만 계산하면 되는데..
def solution(seq, k):
    n = len(seq)
    s = n - 1
    e = n
    while True:
        while sum(seq[s:e]) < k:
            s -= 1
        if sum(seq[s:e]) == k:
            if seq[e - 1] * (e - s) == k:
                s, e = seq.index(seq[e - 1]), seq.index(seq[e - 1]) + (e - s)
            break
        else:
            e -= 1

    return [s, e - 1]

# 내 풀이2 (시간 초과): s는 초기화할 필요가 없었는데 이 때문에 불필요한 부분을 계속 체크해서 시간초과 발생
def solution(seq, k):
    n = len(seq)
    s = n-1
    e = n
    sumSeq = seq[s]
    while True:
        while sumSeq < k:
            s -= 1
            sumSeq += seq[s]
        if sumSeq == k:
            if seq[e-1]*(e-s) == k:
                while s>=1 and seq[s] == seq[s-1]:
                    s-=1
                    e-=1
            break
        else:
            e -= 1
            s = e-1
            sumSeq = seq[s]

    return [s, e-1]

# 내 풀이3 (통과)
# 연속된 부분 수열의 합: 투 포인터 생각
def solution(seq, k):
    n = len(seq)
    s = n-1
    e = n
    sumSeq = seq[s]
    while True:
        while sumSeq < k:
            s -= 1
            sumSeq += seq[s]
        if sumSeq == k:
            if seq[e-1]*(e-s) == k:
                while s>=1 and seq[s] == seq[s-1]:
                    s-=1
                    e-=1
            break
        else:
            e -= 1
            sumSeq -= seq[e]
    return [s, e-1]