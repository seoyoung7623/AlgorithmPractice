# 모음사전 Lv2
'''
itertools 의 product 라이브러리 사용 -> 조합
'''
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort() #조합을 만들고 사전순 정렬.. 이걸 생각못했네
    return words.index(word) + 1
print(solution('AAAE'))