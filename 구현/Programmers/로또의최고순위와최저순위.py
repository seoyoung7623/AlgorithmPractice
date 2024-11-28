# 로또의 최고순위와 최저순위 Lv1
def solution(lottos, win_nums):
    answer = []
    cnt = 0
    win_cnt = 0
    for i in lottos:
        if i == 0:
            win_cnt += 1
        if i in win_nums:
            cnt += 1
    win_cnt += cnt
    for i in win_cnt,cnt:
        if i == 0:
            i += 1
        answer.append(7-i)
    return answer
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
