[내 풀이]
def solution(A, B): # arr1, arr2 로 그대로 두면 가독성이 좋지 않다 : A, B로 바꿔 표현해주기
    answer = []
    for i, A_row in enumerate(A):
        temp = []
        # *B : 가장 바깥 [] 를 날려준다. -> [1,2][3,4][5,6]
        # zip(*B)) : 행과 열을 서로 바꿔 준 효과 !!  [[1,2],[3,4],[5,6]] : [행,행,행] -> [(1,3,5),(2,4,6)] : [열,열]
        for j, B_col in enumerate(zip(*B)):
            k = 0
            for a, b in zip(A_row, B_col):
                k += a*b
            temp.append(k)
        answer.append(temp)
    return answer

[참고 풀이]
- 같은 풀이이지만 리스트 컴프리헨션을 활용해서 짧게 표현한 풀이.
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]