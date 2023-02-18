from collections import Counter


a = input().upper()
count = Counter(a) #가장 많이 쓰는것을 찾을 때는
print(max(count))
print(count)
# max로 하면 되지만 2개 이상
                    #이기에 top
for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            a[i][1] == a[j][1]  #여러번 나옴
            print('?')
            break
        else:
            print(max(count))


#전체 문자.count('찾을 문자')key

