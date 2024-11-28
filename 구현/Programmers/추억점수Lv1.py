# 추억 점수 Lv1
def solution(name, yearning, photo):
    dic = dict()
    result = []
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in photo:
        answer = 0
        for j in i:
            if j in dic:
                answer += dic[j]
        result.append(answer)
    return result