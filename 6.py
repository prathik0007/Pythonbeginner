n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print(0)
else:
    j = 1

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[j] = arr[i]
            j += 1

    print(j)
    print(*arr[:j])