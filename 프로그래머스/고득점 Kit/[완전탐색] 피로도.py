[내 풀이]
maxCount = 0
def dfs(k, dungeons, count):
    global maxCount
    maxCount = max(maxCount, count)
    try:
        for i, dungeon in enumerate(dungeons):
            pilyo, somo = dungeon
            dungeons.pop(i)
            if k >= pilyo:
                dfs(k - somo, dungeons, count + 1)
            dungeons.insert(i, dungeon)
    except:
        print(k, dungeons, count)

def solution(k, dungeons):
    global maxCount
    maxCount = 0
    dungeons = sorted(dungeons)
    dfs(k, dungeons, 0)
    return maxCount

[참고 풀이]
maxCount = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global maxCount
    maxCount = max(maxCount, count)

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return maxCount