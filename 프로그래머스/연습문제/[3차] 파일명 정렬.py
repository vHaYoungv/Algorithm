# 내 풀이
import re
def solution(files):
    answer = files[:]

    p1 = re.compile('[^0-9]+')
    p2 = re.compile('[0-9]+')

    answer.sort(key=lambda file:(p1.search(file).group().lower(), int(p2.search(file).group()), files.index(file)))

    return answer
# 참고풀이
# 1,2,3 순위의 정렬 기준이 있다고 했을 때,
# 3순위의 정렬 기준은 '원래 리스트 순서'라면
# 2순위 정렬, 1순위 정렬 순으로 정렬을 하면 1,2,3순위로 정렬이 된다. 는 접근 방법이 새로웠다.
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b