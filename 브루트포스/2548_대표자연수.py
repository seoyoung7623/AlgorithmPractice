# 2548 대표자연수 S1
'''
중앙값이 정답인 이유는?
절댓값의 특성상, 거리의 합이 최소가 되는 지점은 데이터의 중앙
즉, 중앙값(Median)은 항상 최소 거리를 보장한다!
'''
N = int(input())
arr = list(map(int,input().split()))

arr.sort()

if N % 2 == 0:
    print(arr[N//2-1])
else:
    print(arr[N//2])