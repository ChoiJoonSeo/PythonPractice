
# len(a)
#
# for i in range(len(a)):
#     if len(a) // 2 == 0:
#         if a[i/2-i] == a[i/2+i]
#             print('yes')
#         else:
#             print('no')
#     else
#         if a[i//2]


while True:
    a = input()
    if a == '0':
        break

    # 뒤집어서 바로 비교
    # if a == a[::-1]:
    #     print('yes')
    # else:
    #     print('no')

    a = list(a)
    for i in range(len(a)):
        if a[i] != a[-i-1]: # 투포인터
            print('no')
            break
    else: # break가 안 됐다는 것
        print('yes')

