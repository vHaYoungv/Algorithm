[내 풀이]
from collections import deque
def solution(cacheSize, cities):
    time = 0
    cache = []
    cities = [x.lower() for x in cities]
    if cacheSize==0: return len(cities)*5
    for city in cities:
        if city not in cache:
            time += 5
            if len(cache)==cacheSize:
                cache.pop(0)
            cache.append(city)
        else:
            time += 1
            cache.remove(city)
            cache.append(city)
    return time

[참고 풀이]
# deque에 maxlen을 지정할 수 있다. 용량 초과하면 가장 옛날 것부터 popleft() 된다.
# deque에서도 remove가 된다.
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time