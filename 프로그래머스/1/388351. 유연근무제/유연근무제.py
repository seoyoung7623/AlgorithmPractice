'''
만약 출근 시간이 8시 59분이면 10분 허용이
8시 69분으로 체크됨 따라서 

'''
def to_minutes(hhmm: int) -> int:
    return (hhmm // 100) * 60 + (hhmm % 100)

def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        # 직원 i의 허용 마감 시각(분)
        cutoff = to_minutes(schedules[i]) + 10

        today = startday - 1
        ok = True

        for t in timelogs[i]:
            today = (today + 1) % 7

            # 주말은 이벤트에 영향 없음
            if today == 6 or today == 0:
                continue

            # 늦게 온 경우만 체크
            if to_minutes(t) > cutoff:
                ok = False
                break

        if ok:
            answer += 1

    return answer
