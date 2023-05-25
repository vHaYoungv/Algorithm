[내 풀이]
- 0이 아닌 값이 나올때까지 for 루프를 돌려, 0이 아닌 값이 나오는 인덱스를 찾아 슬라이싱 하는 풀이
def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]

[참고 풀이1]
- 문자열의 왼쪽에서 특정 값을 제거할 때: lstrip('문자') 함수 활용
def solution(n_str):
    return n_str.lstrip('0')

[참고 풀이2]
- 떼야 할 값이 0인 것을 이용한 특수한 풀이
def solution(n_str):
    return str(int(n_str))