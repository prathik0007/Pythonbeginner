n, S = map(int, input().split())
arr = list(map(int, input().split()))

pairs = []

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == S:
            a = min(arr[i], arr[j])
            b = max(arr[i], arr[j])
            pairs.append([a, b])

pairs.sort()

for pair in pairs:
    print(pair[0], pair[1])