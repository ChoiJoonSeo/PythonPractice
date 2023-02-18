T = int(input())

for _ in range(T):
    a, b = input().split()
    a = int(a)
    b = list(b)

    answer = ''
    for num in b:
        answer += num * a  # 'A' * 3

    print(answer)
