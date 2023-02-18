
a = input().strip()

b = 0
if a:
    b += 1

for s in a:
    if s == ' ':
        b += 1

print(b)