a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    c = b[i]/max(b)*100
    c += c
    print(c/a)