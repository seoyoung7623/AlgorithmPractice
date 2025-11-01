T = int(input())

for test_case in range(1, T + 1):
    N, S = input().strip().split()
    N = int(N)
    answer = []
    for i in range(N):
        binary = f"{int(S[i],16):04b}"
        answer.append(binary)
    print(f"#{test_case} {''.join(answer)}")        