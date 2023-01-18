a = 1
b = 1

# 리스트는 같은 값을 보관해도  id가 다르다..
l = [1, 2]
l2 = [1, 2]

# 리스트 내부의 값이 변해도 리스트 id는 안 바뀐다..
print(id(l))
l[0] = 10
print(id(l))

# 숫자를 인덱스로 접근하려면
first_num = str(l[0])[0] # '10'의 0번 인덱스

# + *
l3 = [1, 2, 3]
l4 = [4, 5, 6]
l5 = l3 + l4 # 1, 2, 3, 4, 5, 6

l3[0] = 10
print(l5) # 더하기로 만든 리스트는 새로운 리스트

l3[0] = 1
l6 = l3 * 2
print(l6)
l3[0] = 10
print(l6)

l3[0] = 1
l7 = [l3, l4] # 리스트를 새로 만든게 아니라, 다른 리스트의 껍데기에 그대로 담고 있는 것
l8 = [l3 + l4]
l3[0] = 10
print(l7)
print(l8)


# append insert
# insert <- 처리 시간이 길어질 수도 있다.. (뒤로 한칸씩 다 밀려서)


# del나 pop 모두 음수 인덱스로 제거 가능

# remove는 하나만 없앤다.


# 중첩 리스트 <- 행렬
# N x M 행렬
# 행  열
# 1 2 3 1 = [1,2,3,1]
# 4 5 6 1 = [4,5,6,1]
# 7 8 9 1 = [7,8,9,1]
# y=행, x=열
# [[1,2,3,1],
# [4,5,6,1],
# [7,8,9,1]]
#
# 1xn
# [1,2,3,4,5,1,1,1,1,1]
normal = [1, 2]
nested = [[1, 2], [3, 4], [5, 6]]

for num in normal:
    print(num)

for l in nested:
    for num in l:
        print(num)

l10 = [normal] # [[1, 2]] *normal => [1, 2]
print(normal)
print(*normal)
t = (*normal, *normal) # 리스트가 아니고 튜플이다.
print(t)