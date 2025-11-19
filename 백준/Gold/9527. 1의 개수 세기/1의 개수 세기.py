A,B = map(int,input().split())

def sol(x):
    x+=1
    size = 1
    cnt = 0
    while size < x:
        size <<= 1
    while size >= 2:
        cnt += (x // size) * (size//2)
        if x // (size // 2) % 2 == 1:
            cnt += x % (size // 2)
        size //= 2
    return cnt


print(sol(B) - sol(A-1))