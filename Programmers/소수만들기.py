from itertools import combinations
def solution(nums):
    answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    combi = list(combinations(nums,3))

    for c in combi:
        sumc = sum(c)
        for i in range(2,int(sumc**0.5)+1):
            if sumc%i == 0:
                break
        else: #여기서 else는 루프가 정상적으로 완료 되었을때 실행하는 else이다.
            answer += 1
    return answer

print(solution(	[1, 2, 7, 6, 4]))
