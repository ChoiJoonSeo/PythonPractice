#for i in range(3):
#   a = int(input())
#    a *=a  # 내 예상은 원래 있던 값과의 곱인데
            # 지급은 거듭 제곱이 되고 있다
#    print(a)

#내가 바로 생각나는 것은 count를 써서 구하는것
#키와 값으로 몇개 있는지 [0][1]로 구하는 방법 생각남 --식이 생각이 안나서 찾아봄(counter)



from collections import Counter

a = int(input())
b = int(input())
c = int(input())
d = list(a*b*c)
count = Counter(d)
for i in range(1,9+1):
    print(count(i))

