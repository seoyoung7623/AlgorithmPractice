# 입국심사 Lv3
'''
이분탐색의 접근 방법: 무엇을 범위로 잡고, 무엇을 기준으로 이분 탐색을 진행할것인가?
구해야하는것 : 최소 시간 -> 시간을 기준으로 나눔
나누는 기준 : 해당 분에서 각각의 심사시간을 나누면 심사받을 사람의 수의 합이 총 인원 수보다 크거나 작은 기준
'''
def solution(n, times):
    answer = 0
    min_time = 1
    max_time = max(times) * n
    people = 0

    while min_time <= max_time:
        mid = min_time + (max_time - min_time) // 2
        people = 0
        for time in times:
            people += (mid // time)
            if people >= n:
                break
        if people >= n:
            answer = mid
            max_time = mid -1
        else:
            min_time = mid + 1     
    return answer

print(solution(6,[7,10]))