

for test_case in range(1, 11):
    t = int(input())
    grid = [input().strip() for _ in range(100)]
    cols = [''.join(grid[j][i] for j in range(100)) for i in range(100)]
   
    
    def has_palindrome(L):
        for i in range(100):
            # 가로
            for j in range(100 - L + 1):
                if grid[i][j:j+L] == grid[i][j:j+L][::-1]:
                    #print(grid[i][j:j+L])
                    return True
            # 세로
            for j in range(100 - L + 1):
                if cols[i][j:j+L] == cols[i][j:j+L][::-1]:
                    #print(cols[i][j:j+L])
                    return True
        return False

    ans = 1
    for L in range(100, 0, -1):
        if has_palindrome(L):
            ans = L
            break
    
    print(f"#{t} {ans}")
        