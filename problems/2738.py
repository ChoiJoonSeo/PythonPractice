import sys

n ,m = map(int, input().split())
#N1
A = [list(map(int, input().split())) for _ in range(n)] # 리스트 내포
#N2
B = [list(map(int, input().split())) for _ in range(n)] # 리스트 내포

# A = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
# B = [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
a = [[0] * m for _ in range(n)]
# 0 0 0
# 0 0 0
# 0 0 0

for i in range(n): # 행의 번호
    for j in range(m): # 열의 번호
        a[i][j] = A[i][j] + B[i][j]

#a [[1 ,2 ,3] , [2, 3, 4]]
#*a => [1, 2, 3] [2, 3, 4]


for i in range(n):
    print(*a[i])
#for row in a:
  #  print(*row)


#X = 5 yes
#그 외 no
#같은 문양일떄 합이 5

game_dictionary = {
    "BANANA" : 0,
    "STRAWBERRY": 0,
    "LIME" : 0,
    "PLUM" : 0
}

c = int(input())

for i in range(c):
    a, b = input().split()
    b = int(b)
    game_dictionary[a] += b

for key in game_dictionary:
    if game_dictionary[key] == 5:
        print('YES')
        break
else: # break가 안 됐을 때 실행
    print('NO')



a = input()

for i in range(1, 9+1):
    print(a*i)


if a==0:
    print('no')
else:
    a==1
    N=1
else:
    a==2
    N=2
else:
    a==3
    N=3
else:
    a>=4
    N=4


