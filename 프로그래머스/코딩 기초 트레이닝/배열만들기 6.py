[내 풀이]
def solution(arr):
    stk=[]
    i=0
    while i<len(arr):
        if stk==[]:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
        i+=1
    return stk if stk!=[] else [-1]
[참고 풀이]
- return stk or [-1] : 객체 or 연산. bool(Left Object)가 false이면(비어 있으면) 오른쪽 값을 사용한다!
- stk.append(arr[i])가 중복되니까, 한 가지의 경우로 요약
- while, i=0, i++ 이 for 과 완전히 같으므로 for으로 표현
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]