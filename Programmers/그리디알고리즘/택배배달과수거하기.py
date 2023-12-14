# 택배 배달과 수거하기 kakao 리쿠루트먼트 코테 Lv2
''' 그리디 알고리즘'''
def solution(cap,n,deliveries,pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n-i)*2
    return answer

print(solution(4,5,[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]))

'''
n이 10^6이므로 시간초과 발생
'''
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     deliFlag = False
#     pickFlag = False
#     while True:
#         if deliFlag and pickFlag:
#             break
#         deliload = 0
#         pickload = 0
#         bag = cap
#         for i in range(n-1,-1,-1):
#             if deliveries[i]:
#                 if 0<=deliveries[i]-bag:
#                     deliveries[i] -= bag
#                     bag = 0
#                 else:
#                     bag -= deliveries[i]
#                     deliveries[i] = 0
#                     deliload = max(deliload,i+1)
#                     continue
#             if bag == 0:
#                 deliload = max(deliload,i+1)
#                 break
#         else:
#             deliFlag = True
#         bag = cap
#         for i in range(n-1,-1,-1):
#             if pickups[i]:
#                 if 0<= pickups[i] - bag:
#                     pickups[i] -= bag
#                     bag = 0
#                 else:
#                     bag -= pickups[i]
#                     pickups[i] = 0
#                     pickload = max(pickload,i+1)
#                     continue
#             if bag == 0:
#                 pickload = max(pickload,i+1)
#                 break
#         else:
#             pickFlag = True
#         answer += max(deliload,pickload) * 2
#     return answer

# print(solution(4,5,[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]))