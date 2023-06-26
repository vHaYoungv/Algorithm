# 내 풀이
# 구상 단계에서 한 가지 포인트를 놓쳤더니 코드가 많이 복잡해졌던 점이 아쉽다.
# 한 번 배운 스킬은 다시 배우지 않기 때문에 제약 조건에서 삭제해버릴 수 있다는 것을 간과했기 때문이다.
# 그래서 이미 나올 수 없는 제약 조건을 처음부터 끝까지 확인하느라 복잡해졌다. (skill_list.pop(0))을 하지 않아서.
# 그 외 구조는 모두 같았다.
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        for i, t in enumerate(tree):
            if t not in skill:
                continue
            if any(x not in tree[:i] for x in skill[:skill.index(t)]):
                break
        else:
            answer += 1
    return answer or -1

# 참고풀이
# 제약이 있는 원소들을 모두 찾아낸 다음에, 제약 조건을 처음부터 삭제해나가는 방식 (pop(0))
# 훨씬 직관적
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer