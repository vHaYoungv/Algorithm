def solution(cap, n, deliveries, pickups):
    answer = 0

    # 먼 곳에 배달/수거 하나라도 있으면 제일 먼 곳까지 다녀오기
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    while any(deliveries) != 0 or any(pickups) != 0:
        cnt = 0
        length = 0
        for i, x in enumerate(deliveries):
            if x != 0:
                if x <= cap - cnt:
                    deliveries[i] = 0
                    cnt += x
                else:
                    deliveries[i] = x - (cap - cnt)
                    length = max(length, len(deliveries) - i) #break 문 때문에 break 문 이후의 식 들어가지 않는 것 조심.
                    break
                length = max(length, len(deliveries) - i)
        cnt = 0
        for i, x in enumerate(pickups):
            if x != 0:
                if x <= cap - cnt:
                    pickups[i] = 0
                    cnt += x
                else:
                    pickups[i] = x - (cap - cnt)
                    length = max(length, len(deliveries) - i)
                    break
                length = max(length, len(pickups) - i)
        answer += length * 2
    return answer