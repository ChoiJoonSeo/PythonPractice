a = int(input())


for _ in range(a):
    b = list(input())
    b[0] = b[0].upper()
    print(''.join(b))