arr = list(map(int, input().split()))

current_sum = 0
maximum_sum = 0

for num in arr:
    current_sum = current_sum + num

    if current_sum < 0:
        current_sum = 0

    if current_sum > maximum_sum:
        maximum_sum = current_sum

print(maximum_sum)