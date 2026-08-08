list1 = [1, 2, 3, 4, 5]
list2 = [1, 8, 3]

n = min(len(list1), len(list2))

for i in range(n):
    if list1[i] == list2[i]:
        print(list1[i])