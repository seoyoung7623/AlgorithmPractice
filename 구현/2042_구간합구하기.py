# G1
'''
첫 접근: 구간합이면 누적합?

배열에서 특정 값의 변경이 자주 일어나는경우
누적합처럼 값을 효율적으로 저장할 필요가 있는 경우
'세그먼트 트리'를 이용한다. O(log N)
'''

import sys
input = sys.stdin.readline
class SegmentTree:
    # 초기화
    def __init__(self,arr):
        self.n = len(arr)
        self.tree = [0]*(4*self.n)
        self.build(arr,0,self.n-1,1) # 루트 노드부터 트리 생성
    
    # 세그먼트 트리생성 (재귀))
    def build(self,arr,start,end,node):
        if start == end:
            self.tree[node] = arr[start] # 리프노드
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.build(arr,start,mid,node * 2)
        right_sum = self.build(arr,mid+1,end,node*2+1)
        self.tree[node] = left_sum + right_sum
        return self.tree[node]
    
    # 구간 합
    def sum_query(self,left,right,start,end,node):
        if left > end or right < start: #범위를 벗어난 경우
            return 0
        if left <= start and end <= right: #범위가 포함된 경우
            return self.tree[node]
        
        mid = (start+end)//2
        return self.sum_query(left,right,start,mid,node*2) + \
            self.sum_query(left,right,mid+1,end,node*2+1)
    
    # 값 변경
    def update(self, index, diff, start, end, node):
        if index < start or index > end: # 범위를 벗어나면 무시
            return

        self.tree[node] += diff # 갱신
        if start != end:
            mid = (start + end) // 2
            self.update(index, diff, start, mid, node * 2)
            self.update(index, diff, mid+1, end, node * 2 + 1)
    
    def get_sum(self, left, right):
        return self.sum_query(left,right,0,self.n -1, 1)

    def modify(self, index, new_value,arr):
        diff = new_value - arr[index]
        arr[index] = new_value
        self.update(index, diff, 0, self.n -1, 1)

N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]

seg_tree = SegmentTree(arr)

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        seg_tree.modify(b-1,c,arr)
    elif a == 2:
        print(seg_tree.get_sum(b-1,c-1))