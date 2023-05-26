[내 풀이]
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    else:
        return 1

[참고 풀이]
- 모든 조건을 만족하는지 all()
- 하나라도 조건을 만족하는지 any()
def solution(arr):
    return int(all(arr[i][j] == arr[j][i] for i in range(len(arr)) for j in range(len(arr))))
