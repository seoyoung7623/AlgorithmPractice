'''
장수가 같을때 가장 큰 값 출력
1. 딕셔너리
2. 리스트
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int,input()))
    dic = {}
    for card in cards:
        if card not in dic:
            dic[card] = 1
        else:
            dic[card] += 1
    max_values = max(dic.values())
    answer = [k for k,v in dic.items() if v == max_values]
    print(f"#{test_case} {max(answer)} {max_values}")
        
    
