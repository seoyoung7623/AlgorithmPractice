# 요격 시스템
# def solution(targets):
#     for i in targets:
#         i.append(i[1] - i[0])
#     targets = sorted(targets,key=lambda x : x[2])
#     cnt = 0
#     while targets:
#         cnt +=1
#         for i in targets:
#             if i[0] <= targets[0][0] and targets[0][1] <= i[1]:
#                 targets.remove(i)
#         del targets[0]
#     return cnt
# 시간 복잡도 O(n^2)

def solution(targets):
    targets.sort(key = lambda x: [x[1],x[0]])
    e = 0
    answer = 0
    for target in targets:
        if e <= target[0]:
            answer += 1
            e = target[1]
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))