
#list_a =[]
#for i in range(10):
#    a = int(input())
#    list_a.append(a)  # 이거 없이
                    #내가 생각 한 방법은 a % 42 = b 를 하고
                    # i != j   # list(b[i]) = list(b[j) 이면 list(b[j])를 삭제  for i in range(len(b[i]))
                    #따라서 len(b)의 값이 정답이 된다
#    b = list_a[i] % 42
#    for j in range(len(b)):
#        if b[i] == b[j] and i != j:

s = set() # 얘는 유일한 값만 여러개 저장하고, 순서가 없다.
# {1, 2, 3, 4} 중복된 값이 저장되지 않으니까
for i in range(10):
    a = int(input())
    s.add(a % 42)  #-->str(a%42)??

print(len(s))



