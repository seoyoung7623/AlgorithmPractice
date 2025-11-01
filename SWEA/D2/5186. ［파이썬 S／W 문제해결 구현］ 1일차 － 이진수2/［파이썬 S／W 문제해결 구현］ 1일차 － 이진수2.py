T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = float(input().strip())
    check = 0
    answer = []
    
    for i in range(-1,-13,-1):
        check += 2**(i)
        if check > num:
            answer.append('0')
            check -= 2**(i)
        else:
            answer.append('1')
        if check == num:
            print(f"#{test_case} {''.join(answer)}")
            break
    else:
        print(f"#{test_case} overflow")
        