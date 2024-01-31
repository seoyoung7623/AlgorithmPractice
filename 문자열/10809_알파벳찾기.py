# 10809 알파벳찾기 B2
alphabet_dict = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}
s = input()

for i in range(len(s)):
    if alphabet_dict[s[i]] == -1:
        alphabet_dict[s[i]] = i

print(*alphabet_dict.values())