while True:
    try:
        A, B = map(int,input().split())
        print(A+B)
    except Exception as e: # 확인하는 법
        # print(e)
        break