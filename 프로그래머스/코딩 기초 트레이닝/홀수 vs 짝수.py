[내 풀이]
def solution(num_list):
    odd = 0
    even = 0
    for i, x in enumerate(num_list):
        if i%2 == 0:
            odd += x
        else:
            even += x
    return max(odd, even)

[참고 풀이]
- 리스트 규칙적으로 추출하기 : 슬라이싱 step 활용하기
def solution(num_list):
    return max(sum(num_list[0: len(num_list): 2]), sum(num_list[1: len(num_list): 2]))
