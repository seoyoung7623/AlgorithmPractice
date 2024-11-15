# 1206 view D2
'''
양옆으 2칸사이보다 큰 건물인경우 양옆 건물중 큰 건물값을 뺀값을 더해준다.
왼쪽 사이드, 오른쪽 사이드를 분리해서 그중 가장 큰 건물 현재 건물 - 다음 큰 건물
시간복잡도 O(n)
'''
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    building = list(map(int, input().split()))
    sum=0
    for i in range(2,n-2):
        maxHeight = max(building[i+1],building[i+2],building[i-1],building[i-2])
        if building[i] > maxHeight:
            sum += (building[i] - maxHeight)
    print(f"#{test_case} {sum}")
