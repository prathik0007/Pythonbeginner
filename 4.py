arr = [1, 2, 2, 3, 1, 4, 3]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)