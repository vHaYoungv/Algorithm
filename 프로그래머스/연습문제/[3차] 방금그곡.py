# 내 풀이 : 실패 (86.7) // return '(None)' 을 한 줄 때문에. 해당 하는 값이 없으면 (None)출력 하는 걸 깜박함
def change(music):
    temp = ''
    for i,x in enumerate(music):
        if x == '#':
            s = temp[-1]
            temp = temp[:-1]
            temp += s.lower()
        else:
            temp += x
    return temp

def play(time, music):
    music = change(music)
    length = len(music)
    if time>length:
        answer = music*(time//length)
        answer += music[:time%length]
    else:
        answer = music[:time]
    return answer

def timeDiff(tA, tB):
    return int(tB[0:2])*60+int(tB[3:5]) - (int(tA[0:2])*60+int(tA[3:5]))

def solution(m, musicinfos):
    m = change(m)

    musicinfos = [[i+1]+list(musicinfo.split(',')) for i, musicinfo in enumerate(musicinfos)]
    musicinfos = [[x[0], timeDiff(x[1], x[2]), x[3], play(timeDiff(x[1],x[2]), x[4])] for x in musicinfos]
    musicinfos = sorted(musicinfos, key = lambda x: (-x[1], x[0]))

    for musicinfo in musicinfos:
        if m in musicinfo[3]:
            return musicinfo[2]

# 내 풀이2 : 성공 //
def change(music):
    temp = ''
    for i,x in enumerate(music):
        if x == '#':
            s = temp[-1]
            temp = temp[:-1]
            temp += s.lower()
        else:
            temp += x
    return temp

def play(time, music):
    music = change(music)
    length = len(music)
    if time>length:
        answer = music*(time//length)
        answer += music[:time%length]
    else:
        answer = music[:time]
    return answer

def timeDiff(tA, tB):
    return int(tB[0:2])*60+int(tB[3:5]) - (int(tA[0:2])*60+int(tA[3:5]))

def solution(m, musicinfos):
    m = change(m)

    musicinfos = [[i+1]+list(musicinfo.split(',')) for i, musicinfo in enumerate(musicinfos)]
    musicinfos = [[x[0], timeDiff(x[1], x[2]), x[3], play(timeDiff(x[1],x[2]), x[4])] for x in musicinfos]
    musicinfos = sorted(musicinfos, key = lambda x: (-x[1], x[0]))

    for musicinfo in musicinfos:
        if m in musicinfo[3]:
            return musicinfo[2]
    return '(None)'

# 참고 풀이
def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]