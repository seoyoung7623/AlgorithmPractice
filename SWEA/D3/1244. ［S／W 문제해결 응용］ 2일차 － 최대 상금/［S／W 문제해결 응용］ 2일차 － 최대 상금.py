T = int(input())

for test_case in range(1, T + 1):
    num, cnt = input().split()
    length = len(num)
    numbers = set()
    numbers.add(num)

    for c in range(int(cnt)):
        new_numbers = set()
        for n in numbers:
            for i in range(length-1):
                for j in range(i+1,length):
                    num_cp = list(n)
                    num_cp[i],num_cp[j] = num_cp[j],num_cp[i]
                    new_numbers.add(''.join(num_cp))
                    num_cp[i],num_cp[j] = num_cp[j],num_cp[i]
        numbers = new_numbers
    print(f"#{test_case} {max(numbers)}")