# 1952 달팽이2
# 구현문제, 문제의 일반화를 찾는다
m, n = map(int, input().split(" "))
 
if m > n:
    print(f'{(n*2)-1}') # 세로가 더 클 경우 
else:
    print(f'{(m*2)-2}') # 가로가 더 크거나, 같을 경우
