#불필요한 0은 사용하지 않는다
#특정한 시간에서 -45분
#0 ~ 23까지  a가 0 이고 b가 45보다 작다면 23이 됨
#그게 아니면 a-1
#b의 값은 45-b or 60-(45-b)=15+b

a ,b = map(int, input().split())

if a==0 and b<45:
    print(23, 15+b,end = ' ')
elif b<45:
    print(a-1, 15+b,end = ' ')
else:
    print(a, b-45,end = ' ')
