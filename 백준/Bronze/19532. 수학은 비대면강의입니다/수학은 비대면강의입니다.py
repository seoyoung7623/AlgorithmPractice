a, b, c, d, e, f = map(int, input().split())

denominator = a * e - b * d  # 분모

x = (c * e - b * f) // denominator
y = (a * f - c * d) // denominator

print(x, y)
