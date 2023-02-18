a ,b = map(int,input().split())

c = list(map(int, input().split())) #split을 안 해주니 공백도 리스트에 들어감
answer = []
for i in range(a):
    if c[i] < b:
        answer.append(c[i])
        # print(c[i], end=' ')
print(' '.join(map(str, answer))) # [1, 4, 2, 3]