
# 튜플 ( ) -> 바꿀 수 없는 리스트라고 생각하자. 리스트 [ ] 랑 괄호 표기만 다른 느낌
a = (1, 2, 3) # 쉼표가 있어야 튜플이다.
b = (4, 5) * 2 # (4, 5, 4, 5)
a_val = a[0] # 리스트처럼 인덱스로 접근하면 된다.
c = a + b # (1, 2, 3, 4, 5)

# 괄호 없는 튜플
# 함수 쪽에서 튜플로 리턴을 하면
# 괄호를 딱히 적지 않고 그냥 하나씩 받을 수 있다.
div, mod = divmod(5, 2) # 5 // 2, 5 % 2 => 2, 1


# 함수 매개변수
# 코드는 항상 위에서 아래로 순서대로 진행되고,
# 파라미터의 이름이 달라져도 자기가 할 것을 한다.
def test(asdasd):
    print('test')
    asdasd() # func이 됨


def func():
    print('func') # 출력과 직접적으로 관련있는 코드기 때문에, 역할대로 print를 한다.
    return 1 # 출력이랑은 전혀 관련이 없다. 단지 값만 전달해준다.
    # 함수에 return이 있어도, 굳이 누가 전달 받지 않아도 상관 없음 (전달은 필수가 아님)


for _ in range(5):
    test(func)
# test
# func
# test
# func
# ...

# map, filter
l = [1, 2, 3] # ['1', '2', '3']

# 직관적인 방법
for i in range(3):
    l[i] = str(l[i])

l = map(str, l) # l이라는 자료구조에 들어있는 데이터(element)에 함수를 싹 다 적용시켜서 바꿈

for num in l: # map 객체도 이런 식으로 순서대로 접근할 수 있긴함(for 문으로)
    print(num)

# list에 map 함수를 쓰면 map으로 바뀜. 그래서 list 함수로 감싸줘야됨
l = list(l)

# filter 그 함수에 해당하는 것들만 남김
def is_str(x):
    return x is str # type이 str이면 True를 return

l2 = [1, 2, 3]
l2 = filter(is_str, l2) # 어떤 대상을 걸러내고 싶을 때 사용
print(*l2) # 풀어 헤치기

# 람다 <- 짧은 한줄 짜리 함수를 빠르게 선언할 수 있는 기능
# def product_three(x):
#     return x * 3

product_three = lambda x: x * 3 # 람다 선언
# lambda 파라미터: 함수식
print(product_three(3))


# 제네레이터 <- 개념을 아는 게 중요. 실전에서는 사용할 일이 딱히 없다.
def gene(): # next() 명령을 받으면 yield를 만날 때까지 진행
    print(1)
    print(2)
    yield 'first' # 나중에 명령을 받으면 'first'를 return 하겠다.
    print(3)
    yield 'second'
    print(4)
    yield 'third'

g = gene()
first = next(g) # 제네레이터는 next라는 함수와 같이 쓰인다.
sec = next(g)

g2 = gene()
for y in g2: # for문이랑 제네레이터를 같이 쓰면 자동으로 next를 쓴다.
    continue

# 함수, 람다 써보는 느낌으로 푸는 문제: 15964번
# 가변 매개변수 써보기: 2475번
# 2차원 리스트, for문: 2738번


A, B = map(int, input().split())# 공백으로 구분된 문자들을 한번에 다 바꿀 때
# split 쓰고, map을 사용

def func(A, B):
    return (A+B)*(A-B)

AB = func(A, B)
print(AB)


a, b, c, d, e = map(int, input().split())

a **= a
b **= b
c **= c


