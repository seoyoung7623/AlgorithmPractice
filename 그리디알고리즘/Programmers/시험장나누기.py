# 시험장 나누기 P5
# 파라매트릭 서치, 트리, 그리디
'''
최소화된 최대 그룹의 인원을 직접 구하는 것 보다
각 그룹의 수를 x명으로 제한할때 그룹의 수가 k개 이하인지 판단하는(이분탐색) -> 결정문제인 파라매트릭 서치 방법을 이용한다.
리프에서 올라가며 그룹의 정원이 차지 않을때까지 최대한 그룹 생성ㅇ을 미루고 올려보낸다. -> 그리디
'''
import sys
sys.setrecursionlimit(10**6)
l = [0]*10005
r = [0]*10005 
x = [0]*10005 #시험장의 응시인원
p = [-1]*10005 #부모 노드 번호
n = 0 # 노드의 수
root = 0 #루트
cnt = 0 #그룹의 수

# cur: 현재보는 노드 번호, lim: 그룹의 최대 인원 수
def dfs(cur,lim): # 루트, min
    global cnt
    lv = 0
    if l[cur] != -1: #왼쪽 자식노드 있는 경우
        lv = dfs(l[cur],lim) #왼쪽자식을 루트로 보내 중간 계산
    rv = 0 #오른쪽 자식 트리에서 넘어오는 인원 수
    if r[cur] != -1: #오른쪽 자식노드 있는 경우
        rv = dfs(r[cur], lim)
    # 1. 왼쪽 자식 트리와 오른쪽 자식 트리에서 넘어오는 인원을 모두 합해서 lim 이하일 경우
    if x[cur] + lv + rv <= lim:
        return x[cur] + lv + rv
    # 2. 왼쪽 자식 트리와 오른쪽 자식 트리에서 넘어오는 인원 중 작은 것을 합해도 lim이하일 경우
    if x[cur] + min(lv,rv) <= lim:
        cnt += 1 # 둘 중 큰 인원은 그룹을 지어버림
        return x[cur] + min(lv,rv)
    
    #3. x가 클경우
    cnt += 2
    return x[cur]

def solve(lim): #lim은 min
    global cnt
    cnt = 0
    dfs(root,lim)
    cnt += 1
    return cnt

def solution(k, num, links): #k 나눌 그룹/ num 응시자 수 /link 노드
    global root
    n = len(num) # 노드 개수

    #왼쪽, 오론쪽 자식노드 ,부모 노드 저장
    for i in range(n):
        l[i],r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1: 
            p[l[i]] = i #부모너드가 무엇인지 기록
        if r[i] != -1:
            p[r[i]] = i
    for i in range(n):
        if p[i] == -1: #부모노드가 없는 경우 루트 노드가 됨
            root = i
            break
    st = max(x) # 시험장 응시인원의 최댓값 L
    en = 10 ** 8 # R
    while st<en: #최댓값이 en보다 작을 경우
        mid = (st+en) // 2 
        if solve(mid) <= k: # 그룹수보다 작을 경우
            en = mid
        else: st = mid + 1
    return st

print(solution(3,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))