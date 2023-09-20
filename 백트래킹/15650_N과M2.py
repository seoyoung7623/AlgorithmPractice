# 15650 N과 M 2 S3
N,M = map(int,input().split())
arr = [i for i in range(1,N+1)] #1~N 까지 값을 넣어줌
result = []
def backtrack(start,backList):
    if len(backList) == M:
        result.append(list(backList)) #리스토 새로 정의 안해주면 pop할때 같이 빠짐!
        return
    for i in range(start,len(arr)):
        backList.append(arr[i])
        backtrack(i+1,backList) # i는 back 트래킹 범위
        backList.pop()
backtrack(0,[]) # 0번 인덱스부터 start
for i in result:
    print(*i)