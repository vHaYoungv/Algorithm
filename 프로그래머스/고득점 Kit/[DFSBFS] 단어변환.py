visited = []
minLevel = 0


def solution(begin, target, words):
    global visited
    global minLevel
    words.append(begin)
    visited = [False] * len(words)
    length = len(words)
    minLevel = length

    for i, word in enumerate(words):
        if target == word:
            visited[i] = True
            break
    else:
        return 0

    def dfs(level, now):
        global minLevel
        if level > minLevel:
            return
        if now == begin:
            minLevel = level
            return
        else:
            for i, word in enumerate(words):
                if not visited[i] and isChangeable(word, now):
                    visited[i] = True
                    dfs(level + 1, word)
                    visited[i] = False

    dfs(0, target)

    return minLevel


def isChangeable(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False
