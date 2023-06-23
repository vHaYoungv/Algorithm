# 내 풀이
def solution(record):
    nickById = {(rec + ' ').split(' ')[1]: (rec + ' ').split(' ')[2] for rec in record if
                (rec + ' ').split(' ')[0] != 'Leave'}

    answer = []
    for rec in record:
        action, id, nick = (rec + ' ').split(' ')[:3]
        if action == 'Enter':
            answer.append("%s님이 들어왔습니다." % (nickById[id]))
        if action == 'Leave':
            answer.append("%s님이 나갔습니다." % (nickById[id]))
    return answer

# 내 풀이2
# printer를 이용하니 if문이 줄어 상대적으로 깔끔해 보이는 듯 하다.
def solution(record):
    nickById = {(rec + ' ').split(' ')[1]: (rec + ' ').split(' ')[2] for rec in record if
                (rec + ' ').split(' ')[0] != 'Leave'}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    answer = []
    for rec in record:
        action, id, nick = (rec + ' ').split(' ')[:3]
        if rec.split(' ')[0] != 'Change':
            answer.append(nickById[id]+printer[action])
    return answer

# 참고 풀이
# 출력 문구도 딕셔너리 활용
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer