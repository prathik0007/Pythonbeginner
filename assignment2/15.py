s = input("Enter a string: ")

seen = set()
left = 0
maximum = 0

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    if length > maximum:
        maximum = length

print("Longest length:", maximum)