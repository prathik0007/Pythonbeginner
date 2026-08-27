from functools import cmp_to_key

arr = input("Enter numbers: ").split()

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

arr.sort(key=cmp_to_key(compare))

answer = ''.join(arr)

print("Largest number:", answer)