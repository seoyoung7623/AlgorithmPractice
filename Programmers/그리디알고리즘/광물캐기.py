# 광물캐기 Lv2 
# 그리디 알고리즘
def solution(picks, minerals):
    answer = 0
    sum = 0
    # 1. 곡갱이의 수 *5 만큼 광석을 캘수 있다.
    for i in picks:
        sum += i*5
    # 총 개수보다 큰 경우 잘라준다. 뒤에는 사용할 수 없기 때문
    if sum<len(minerals):
        minerals = minerals[:sum]
    
    # 광물을 연속해서 5개 캐야하므로 5개씩 잘라서 리스트에 저장해준다!
    new_minerals = [[0,0,0] for _ in range(len(minerals)//5 + 1)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i//5][0] += 1 #5개씩이므로 앞인덱스는 i//5!
        elif minerals[i] == 'iron':
            new_minerals[i//5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i//5][2] += 1

    # 광물을 다이아,철,돌 순서대로 정렬! lamba에서 -x 음수 사용 주의(큰수부터 나열하기 위해)
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))

    #광문 다이아,철,돌 순서대로 캔다. 그리디접근
    #광물들을 기준으로 도구를 반복!
    for i in new_minerals:
        dia,iron,stone = i
        for j in range(len(picks)): # 광물리스트안에 곡갱이 리스트 이중반복문 설계 주의
            if picks[j]>0 and j==0: # j==0: 다이아몬드도구인 경우!
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j ==1:
                picks[j] -= 1
                answer += dia*5 + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += dia*25 + 5*iron + stone
                break

    return answer
print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))