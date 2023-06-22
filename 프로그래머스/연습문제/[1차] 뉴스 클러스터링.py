# 내 풀이
import re
from collections import Counter
def solution(str1, str2):
    p = re.compile('[a-zA-Z]{2}')
    aCnt = Counter([str1[i:i + 2].lower() for i in range(len(str1) - 1) if p.match(str1[i:i + 2])])
    bCnt = Counter([str2[i:i + 2].lower() for i in range(len(str2) - 1) if p.match(str2[i:i + 2])])

    keys = aCnt.keys() | bCnt.keys()
    n = sum(min(aCnt[key], bCnt[key]) for key in keys)
    d = sum(max(aCnt[key], bCnt[key]) for key in keys)

    return (int((n / d) * 65536) if d != 0 else 65536)

# 참고 풀이
# re.findall()이랑 p.match()
import re
import math
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)