T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0]*(N+1)
    num = 1
    
    def in_order(node):
        global num
        if node <= N:
            in_order(node*2)
            tree[node] = num
            num += 1
            in_order(node*2+1)
    
    in_order(1)
    print(f"#{test_case} {tree[1]} {tree[N//2]}")
    