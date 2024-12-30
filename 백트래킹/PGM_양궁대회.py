'''
https://school.programmers.co.kr/learn/courses/30/lessons/92342
Lv2 지만 난이도헬
백트래킹 풀이
'''
def solution(n, info):
    # 결과를 저장할 변수
    max_diff = 0
    answer = [-1]
    
    # DFS를 사용하여 모든 경우를 탐색
    def dfs(idx, arrows_left, ryan_scores): # arrows_left = n(남은 화살의 개수)
        nonlocal max_diff, answer
        
        # 화살을 모두 사용했거나, 모든 점수를 탐색한 경우
        # 백트래킹 종료조건
        if arrows_left == 0 or idx == 11:
            ryan_scores[10] += arrows_left  # 남은 화살을 0점에 배치 점수에 영향을 주지 않음
            apeach_score = 0
            ryan_score = 0
            
            # 점수 계산
            for i in range(11):
                if info[i] == 0 and ryan_scores[i] == 0:
                    continue
                if ryan_scores[i] > info[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i
            
            # 점수 차이 계산
            diff = ryan_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                answer = ryan_scores[:]
            elif diff == max_diff:
                # 사전순으로 더 낮은 점수를 많이 맞힌 경우를 선택
                for i in range(10, -1, -1):
                    if ryan_scores[i] > answer[i]:
                        answer = ryan_scores[:]
                        break
                    elif ryan_scores[i] < answer[i]:
                        break
            ryan_scores[10] -= arrows_left  # 복원
            return
        
        # Apeach의 점수보다 하나 더 맞추는 경우
        # DFS 백트레킹
        if arrows_left > info[idx]:
            ryan_scores[idx] = info[idx] + 1
            dfs(idx + 1, arrows_left - ryan_scores[idx], ryan_scores)
            ryan_scores[idx] = 0  # 복원
        
        # ⭐️ 해당 점수를 포기하는 경우: 인덱스를 그냥 넘겨줌
        dfs(idx + 1, arrows_left, ryan_scores)
    
    # DFS 시작
    dfs(0, n, [0] * 11)
    
    return answer

print(solution(9,[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))