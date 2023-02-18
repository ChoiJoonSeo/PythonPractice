if True:
    print('참')

while True: # 멈추는 포인트가 없으면 멈추지 않는데, 반복하는 것 자체가 자원을 잡아먹는 행동
    print('참')
    break # 만나면 무조건 여기서 멈춘다. while문의 조건이 아직 참이더라도
    print()

for i in range(10):
    if i == 5:
        continue # 내 순서는 바로 끝나고, 바로 다음 순서로 넘어가서 코드 다시 진행

    print(i)
    pass

i = 0
while i < 10: # for문처럼 쓸거면 그냥 for문 쓰는 게 낫다.
    i += 1

answer = 1
while answer < 100000: # 언제 멈출지 잘 모르지만 멈춰야 되는 기준만 안다면, while문이 좋다.
    answer *= i
    i += 1

# remove + while
# remove의 단점이자 장점은: 하나만 없앤다 값이 여러개라도
l = [1, 2, 2, 2]
while 2 in l:
    l.remove(2) # REMOVE <- 값을 기준으로 삭제 (인덱스가 아님)
    # 값은 아는데 리스트의 어느 위치에 있는지 모를 때, REMOVE랑 WHILE을 같이 쓰면 다 제거할 수 있음

# continue
idx = 0
while idx < 10:
    idx += 1

    if idx % 2 != 0:
        continue # 홀수일 때는 더이상 진행 안 한다.
    print(idx)

