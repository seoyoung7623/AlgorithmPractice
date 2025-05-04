X = int(input())
line = 1
while line < X:
    X -= line #line에서 몇번째인지 알 수 있음
    line += 1

if line % 2 == 0:
    numerator = X
    denominator = line - X + 1
else:
    numerator = line - X + 1
    denominator = X

print(f"{numerator}/{denominator}")
