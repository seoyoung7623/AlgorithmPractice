# PGM 퍼즐게임 챌린지 Lv2
'''
이분탐색
'''
def solution(diffs, times, limit):
    answer = 0
    start = min(diffs)
    end = max(diffs)

    # 레벨을 지정하는 부분
    while start<=end:
        # 첫문제 풀고 시작
        total_time = times[0]
        level = (start + end)//2
        # 총 시간을 계산
        for i in range(1,len(diffs)):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                total_time += (diffs[i]-level)*(times[i]+times[i-1])+times[i]
        # 시간 초과
        if total_time > limit:
            start = level+1
        else:
            answer = level
            end = level-1
    return answer

print(solution([1,5,3],[2,4,7],30))
print(solution([1, 4, 4, 2],[6, 3, 8, 2],59))
print(solution([1, 328, 467, 209, 54],[2, 7, 1, 4, 3],1723))