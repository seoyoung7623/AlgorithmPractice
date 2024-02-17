# 징검다리 Lv4
'''
이분탐색
바위사이의 길이를 범위로 잡고, 그 길이에 제거할수 있는 바위를 탐색한다.
'''
# def solution(distance, rocks, n):
#     answer = 0
#     left = 0
#     right = distance
#     cnt = 0
#     while left <= right:
#         mid = (left + right)//2
#           #지정한 바위사이의 길이에서 징검다리 제거를 진행해야함 -> 반복문 필요
#         if cnt == n:
#             answer = mid
#             break
#         if right-left >= mid:
#             answer = mid
#             left = rocks[]
#         elif right-left < mid:
#             right

#     return answer

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left = 1
    right = distance

    answer = 0

    while left <= right:
        mid = (left+right)//2

        cur_rock = 0 #왼쪽바위
        cnt = 0
        for i in range(len(rocks)):
            pre_rock = rocks[i]

            if pre_rock - cur_rock < mid: #바위사이가 작으면
                cnt += 1 #바위제거
            else:
                cur_rock = pre_rock #다음바위를 왼쪽바위로 지정
        if cnt <= n: #제거해야할 바위가 남아있는경우
            answer = mid
            left = mid + 1
        else:
            right = mid -1
    return answer
print(solution(25,[2, 14, 11, 21, 17],2))