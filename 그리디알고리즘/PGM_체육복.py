# 체육복 Lv1

# 내 코드
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     lost.sort()
#     reserve.sort()
#     for i in reserve:
#         if i in lost:
#             lost.remove(i) #반복문을 돌면서 lost의 값이 삭제되는 위험이 있음
#             answer += 1
#         elif i-1 in lost:
#             lost.remove(i-1)
#             answer += 1
#         elif i+1 in lost:
#             lost.remove(i+1)
#             answer += 1       
#     return answer


# 참고코드
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    # 마지막 코드에서 lost의 학생을 지우게 되므로 여벌옷을 가졌지만 잃어버린 학생을 먼저 중복 처리해주고 계산해야한다.
    for i in reserve[:]: # reserve 복사
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1) 
        elif i+1 in lost:
            lost.remove(i+1)  
    answer = n - len(lost)
    return answer