[내 풀이]
def solution(myStr):
    res = myStr.split('a')
    temp = []
    for x in res:
        temp += x.split('b')
    ans = []
    for x in temp:
        ans += x.split('c')
    ans = [x for x in ans if x != '']
    return ans if len(ans)!=0 else ["EMPTY"]

[참고 풀이]
- 구분자 a, b, c 는 모두 같은 역할을 하기 때문에, 하나의 다른 문자로 바꿔버리고 같은 취급을 해버리는 것이 핵심
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']