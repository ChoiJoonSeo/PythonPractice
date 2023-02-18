#enumerate
l = [10, 20, 30, 40]

for idx, num in enumerate(l):
    print(idx, num)

# 리스트 내포 = 리스트 컴프리헨션
l2 = []
for i in range(100):
    if i % 2 == 0:
        l2.append(i)



l2 = [i for i in range(100)] # 윗 코드를 한줄로 적을 수 있다.
l2 = [i for i in range(100) if i % 2 == 0] # 짝수만 넣고 싶을 때


# join
output = []
for i in range(1, 5 + 1):
    output.append('*' * i)
print('\n'.join(output))
