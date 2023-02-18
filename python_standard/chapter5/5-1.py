def plus(x, y): # 함수에서만 따로 쓰는 a, b
    return x + y # return이 출현하면 그냥 함수 무조건 끝난다는 얘기
    # return을 발동시키지 않으면 아무값도 안 돌려줌

def test(*a): # 전달인자가 여러개일거라고만 추측하고, 동작
    result = 0

    for num in a:
        result += num

    return result

def test2(x, y, *z):
    print(x)
    print(y)
    print(*z)

# 기본 매개변수
def test3(a=1, b=2): # 기본값이 있는 파라미터
    for _ in range(a):
        print('프린트')

# 일반 - 가변 - 기본 파라미터 순서로 작성해야된다.
# 근데 코딩테스트에서는 사실 일반만 쓸줄 알아도 괜찮음.
def test4(x, *y, z=1):
    pass

# 그냥 return
def test5():
    print('하이')

    for i in range(5):
        break # for문만 끝남 (얘가 속한 영역의 반복문만 딱 끝냄, 함수까지 끝내지는 않음)

    return # 함수가 아예 끝남, None을 리턴
    print('하이')


# a = input("입력 해주세요: ")
# 괄호 안에 들어가는 것 => 매개변수(파라미터 parameter)
# 리턴값 = 함수의 결과로 전달하는 값

# None
a = plus(3, 1) # 함수를 실행 => 호출(부른다)
b = plus(5, 2)
plus(7, 3) # 재사용 하는데 강점이 크다.
c = test(1, 2, 3, 4, 3, 5, 6, 7, 8)
test2([1, 2, 3], 4)
test2(1, 2, 3, 4)
test3(a=10)
# 키워드 매개변수 (내가 값을 바꿀 대상을 특정할 때)

a = len('안녕하세요')



def kl(g, h):
    print(g + h)
    return(g + h)
e = kl(3, 4)
f = kl(1, 2)

print(e)



def test6(a=1):
    for i in range(a):
        print('kkk')
    return 23


r = test6(a=3)
print(r)



