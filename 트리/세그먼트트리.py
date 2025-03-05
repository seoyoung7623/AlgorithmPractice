'''
✅ 세그먼트트리 주요연산
1. 초기화 O(N)
2. 구간 합 질의 O(log N)
3. 값 변경 O(log N)

💡 언제 사용하는가?
배열의 특정 범위의 합을 자주 구해야 할 때
배열의 특정 값을 빠르게 업데이트해야 할 때
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
