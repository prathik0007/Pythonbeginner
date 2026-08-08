T = int(input())

for _ in range(T):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    freq = {}
    pairs = []

    for num in arr:
        complement = target - num

        if complement in freq:
            for _ in range(freq[complement]):
                a = min(num, complement)
                b = max(num, complement)
                pairs.append([a, b])

        freq[num] = freq.get(num, 0) + 1

    pairs.sort()

    if len(pairs) == 0:
        print("-1 -1")
    else:
        for pair in pairs:
            print(pair[0], pair[1])