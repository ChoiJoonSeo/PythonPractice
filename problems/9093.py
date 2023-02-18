a = int(input())


for i in range(a):
    b = input()

    b[::-1] # 이러면 전부다 뒤집어 출력
            #기준이 필요함 ''<- 뛰어쓰기를 기준으로 만약 뛰어쓰기가 몇개인지
            #기준이 있다면 구할 수 있음 [i:j:-1]이러한 형식으로 가능 할 듯

    list_b = b.split()
    for i in range(len(list_b)):
        list_b[i] = list_b[i][::-1]
    print(' '.join(list_b))