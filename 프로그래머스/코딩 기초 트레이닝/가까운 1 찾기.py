[내 풀이]
def solution(arr, idx):
    for i, x in enumerate(arr):
        if i>=idx and x==1:  return i
    return -1

[참고 풀이]
- try-except: 구문 try에서 예외가 발생하면 except가 실행됨
- index(찾을 값, 시작 인덱스): 두번 째 인자는 시작 인덱스구나.
def solution(arr, idx):
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
    return answer