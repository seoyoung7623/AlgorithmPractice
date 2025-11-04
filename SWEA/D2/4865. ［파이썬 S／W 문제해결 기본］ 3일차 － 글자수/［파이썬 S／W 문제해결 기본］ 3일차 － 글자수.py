T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    dic = {}
    for s in str1:
        if s not in dic:
            dic[s] = 0
   	
    for s in str2:
        if s in dic:
            dic[s] += 1
    answer = max(dic.values())
    print(f"#{test_case} {answer}")
        