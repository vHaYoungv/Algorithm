[내 풀이]
- try-except 구문을 이용해서 오류 발생시 다른 로직이 작동하도록 한다
def solution(arr):
    try:
        if (arr[::-1].index(2)==0):
            return arr[arr.index(2):]
        return arr[arr.index(2):-(arr[::-1].index(2))]
    except:
        if 2 not in arr:
            return [-1]

[참고 풀이]
- -1, -2, -3 과 같이 리스트 값을 찾으려 할 때 문제가 발생하는 것이기 때문에 len(arr)을 이용해서 양수인덱스로 표현하도록 한다
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
