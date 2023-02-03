a = int(input())
for i in range(a):
    OX = input()

    o_cnt = 0 # 연속된 O의 개수
    # O O X X O X X O O O

    answer = 0
    flag = False # 연속되고 있는 상태
    for alphabet in OX:
        if alphabet == 'O':
            if flag:
                o_cnt += 1
            else: # 연속되고 있지 않는 상태다..
                o_cnt = 1
                flag = True
            answer += o_cnt
        else: # 'X' 일때
            flag = False
    print(answer)