[내 풀이]
import heapq as hq

# 특정 시간 소요 배치 (힙)
def solution(book_time):
    # book_time 값 정리
    book_time = [[int(x[0][:2]) * 60 + int(x[0][3:5]), int(x[1][:2]) * 60 + int(x[1][3:5])] for x in book_time]

    # 시작 시간 이른 순 정렬 먼저
    book_time.sort()

    # 메인 루프
    room = []
    hq.heappush(room, 0)
    clean_time = 10
    for check_in, check_out in book_time:
        if room[0] + clean_time <= check_in:
            hq.heappop(room)
            hq.heappush(room, check_out)
        else:
            hq.heappush(room, check_out)
    return len(room)

[참고 풀이]
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)
