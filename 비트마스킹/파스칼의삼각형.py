# 조합문제중 하나
def pascal_triangle(n):
    triangle = [[1]]
    
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

print(pascal_triangle(5))