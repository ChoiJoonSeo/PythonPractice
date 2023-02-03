#10952
while True: # while 문 뒤에는 if문처럼 Boolean값을 결과로 내는 조건문 사용
    a, b = map(int, input().split())

    if a == 0 and b == 0: break # 둘다 0 이면 멈춤

    print(a + b)