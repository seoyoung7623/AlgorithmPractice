# 11054 가장 긴 바이토닉 부분 수열 G4
# 바이토닉 접근방법 -> 리스트를 뒤집어서 증가하는 부분수열을 체크한다.
N = int(input())
arr = list(map(int,input().split()))
reverse = arr[::-1]

increase = [1] * N
decrease = [1] * N
result = [0] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i],increase[j]+1)
        if reverse[i] > reverse[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

for i in range(N):
    result[i] = increase[i]+decrease[N-i-1]-1
print(max(result))