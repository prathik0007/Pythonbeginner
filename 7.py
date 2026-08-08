n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rows = set()
columns = set()

# Find original zeros
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            rows.add(i)
            columns.add(j)

# Make rows zero
for i in rows:
    for j in range(m):
        matrix[i][j] = 0

# Make columns zero
for j in columns:
    for i in range(n):
        matrix[i][j] = 0

# Print matrix
for row in matrix:
    print(*row)