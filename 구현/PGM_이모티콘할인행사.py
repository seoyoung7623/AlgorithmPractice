# PGM 이모티콘 할인행사 Lv2
'''
완전 탐색
할인율이 10,20,30,40으로 정해져있고 이모티콘마다 할일율을 조합하여 완전 탐색한다.
이모티콘마다 유저의 구매금액을 계산, 구매한 금액은 최적의 금액으로 갱신한다.
'''
from itertools import product

def solution(users, emoticons):
    discount_rates = [10,20,30,40]
    answer = [0,0] #가입자 수, 총판매액

    # 각 이모티콘마다 할인율을 조합
    discount_combination = product(discount_rates,repeat=len(emoticons))
    # 할인율
    for discounts in discount_combination:
        # print(discounts)
        total = 0
        subscribers = 0

        # 유저 이모티콘 계산
        for user_discount,user_limit in users:
            user_total = 0

            # 할인율이 높으면 유저가 이모티콘을 삼
            for emoticon, discount in zip(emoticons,discounts):
                if discount >= user_discount:
                    user_total += emoticon * (1-discount/100)
            
            if user_total >= user_limit:
                subscribers += 1
            else:
                total += user_total

        # 최적결과 갱신
        if subscribers > answer[0] or (subscribers == answer[0] and total > answer[1]):
            answer = [subscribers,int(total)]
    return answer

print(solution(	[[40, 10000], [25, 10000]], [7000, 9000]))

