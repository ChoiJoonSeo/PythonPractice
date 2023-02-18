a, b = input().split()
a = a[::-1] # a가 갖고 있던 것을 버리고 a[::-1]
b = b[::-1]

a = int(a)
b = int(b)

if a>=b:
    print(a)
else:
    print(b)



if a[2]>b[2]  #크기 구분은 가능 하지만 결과적으로 출력이 힘듬
    print(a)    #내가 생각한 이 방법은 자리 숫자마다 비교해서 구하는것

c = a[0]
d = b[0]
a[0] = a[2]
a[2] = c
b[0] = b[2]
b[2] = d

if a>=b:
    print(a)
else:
    print(b)


#문제의 숫자가 세자리수이기 때문에 첫번쨰와 세번쨰 숫자만 바꾸면 답이 나옴
#인덱스로 바꾸면 첫째와 셋째수가 같아 지기때문에 저장을 통해

 c = list(a[0])
 d = list(b[0])
list(a[0]) = list(a[2])
list(a[2]) = c
list(b[0]) = list(b[2])
list(b[2]) = d
