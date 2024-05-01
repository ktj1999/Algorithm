from heapq import heappop, heappush

def time_to_minutes(time_str):
    # 문자열 형태의 시간을 분 단위로 변환하는 함수
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    books, rooms = [], []
    for bt in book_time:
        s, e = bt
        sh, sm = s.split(":")
        eh, em = e.split(":")
        st, et = int(sh)*60+int(sm), int(eh) * 60 + int(em)

        # 시작 시각이 자정을 넘어가는 경우, 해당 예약을 다음 날로 처리
        if st < 1440:  # 자정(24 * 60)을 넘어가지 않는 경우
            heappush(books, [st, et])
        else:  # 자정을 넘어가는 경우
            heappush(books, [st - 1440, et])  # 시작 시각을 다음 날로 조정하여 예약 추가

    while books:
        st, et = heappop(books)
        if not rooms:
            rooms.append([et, st])
        else:
            room = heappop(rooms)
            if room[0] + 10 > st:
                heappush(rooms, room)
                heappush(rooms, [et, st])
            else:
                room = [et, st]
                heappush(rooms, room)
    answer = len(rooms)
    return answer