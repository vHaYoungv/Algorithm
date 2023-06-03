# 내 풀이

# 참고풀이
- 정렬을 하면, 바로 다음 것만 접두사인지 확인하면 된다 따라서 O(n)
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
