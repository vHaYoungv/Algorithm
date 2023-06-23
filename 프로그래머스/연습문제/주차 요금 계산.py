# 내 풀이
def solution(fees, records):
    cars = []
    answer = []
    dic_IN = {}
    dic_TIME = {}

    # dic_IN : 차량 별 입차시간 (출차 시 기록 삭제)
    for rec in records:
        hhmm, car, io = rec.split(' ')
        if car not in cars:
            cars.append(car)
        m = 60*int(hhmm[:2]) +int(hhmm[3:5])
        if io == 'IN':
            dic_IN[car] = m
        elif io == 'OUT':
            M = dic_IN.pop(car)
            dic_TIME[car] = dic_TIME.get(car, 0) + m-M

    # dic_TIME : 차량 별 주차시간
    for key in dic_IN.keys():
        m = dic_IN[key]
        dic_TIME[key] = dic_TIME.get(key, 0) + 23*60+59-m

    # answer : 주차요금 계산
    for car in sorted(cars):  # 주차요금 계산 #여기서 car번호 별로 정렬하면 된다. record 자체를 정렬하려고 하다간 데이터가 이상하게 정렬되어버린다.
        v = dic_TIME[str(car)]
        if v <= fees[0]:
               answer.append(fees[1])  # 기본요금
        else:
            v -= fees[0]  # 추가요금
            if v % fees[2] != 0:  # 올림처리
                v += (fees[2] - v % fees[2])
            answer.append(fees[1] + (v // fees[2]) * fees[3])
    return answer
# 참고풀이
