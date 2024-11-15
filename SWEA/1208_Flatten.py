# 1208 Flatten D2
'''
덤프 횟수 n
가장 높은을 줄이면 가장 낮은곳이 채워짐
리스트로 정렬하고 가장 뒤에꺼 -1 가장 앞에꺼 +1 정렬하고
'''
T = 10
for test_case in range(1,T+1):
    n = int(input())
    box = list(map(int, input().split()))
    for i in range(n):
        box.sort()
        # 평탄화상태
        if box[0] == box[len(box) - 1]:
            break
        elif box[0]+1 == box[len(box) - 1]:
            break
        box[0] += 1
        box[len(box) - 1] -= 1
    box.sort()
    print(f'#{test_case} {box[-1]-box[0]}')
