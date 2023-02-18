
# list_a = [int(input()) for _ in range(9)]
list_a = []
for i in range (9):
    b = int(input())
    list_a.append(b)

max_val = max(list_a) # max를 쓰면 수 전부를 확인
for j in range(9):
    if list_a[j] == max_val:
        print(max_val)
        print(j+1)
        break

a_val, a_idx = -1, -1
for i in range(9):
    b = int(input())

    if a_val < b:
        a_val = b
        a_idx = i + 1
print(a_val, a_idx, sep='\n')

#
# l = sorted(list(enumerate(list_a)), key=lambda x: x[1])
# print(l[-1][1])
# print(l[-1][0] + 1)



#    a = list(input())
print(list_a)

#if a[i] == max(a):
#
#    print(a[i])
#    print("i")



