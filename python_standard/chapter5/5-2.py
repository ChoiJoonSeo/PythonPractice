def test(a):
    if a == 500: # 500에서 더이상 진행 안 하겠다는 얘기
        return # 재귀를 멈추는 방법

    print(a)
    test(a+1) # 재귀함수 (함수 안에서 똑같은 함수를 다시 부름)


def factorial(n): # 재귀로 팩토리얼 구하기
    if n == 1: # 재귀함수를 멈추는 시점
        return 1

    return n * factorial(n - 1)
# 재귀는 개념 자체가 어렵다.
# 그래서 이해하려면 순서대로 적어보는 게 도움이 된다.
# 재귀의 단점: 함수를 연속으로 부르는 게 자원을 많이 잡아먹음
# 파이썬은 함수를 호출할 때마다, 함수에 대한 정보를 메모리에 저장
# 재귀함수를 마구잡이로 호출하면 메모리가 감당할 수가 없음

result = factorial(5)

# 피보나치 수열
def fibo(idx):
    if idx == 0 or idx == 1:
        return 1
    else:
        return fibo(idx - 1) + fibo(idx - 2)

list_a = [1, 1]
# list_a[2] = list_a[0] + list_a[1]
# list_a[3] = list_a[1] + list_a[2]
for i in range(30):
    list_a.append(list_a[-1] + list_a[-2])


fibo(100) # 이미 여기서 구했음
fibo(100) # 구한 걸 또 구함
# 구했던 것을 기록해두어야 비효율적인 작업이 일어나지 않음
# 메모리 효율적으로 코드를 짤 것인지, 시간 효율적으로 코드를 짤 것인지
# 기록한다. <- 메모리 효율적이기 보다는, 시간 효율적으로 코드를 짜겠다.
# 기록 => 메모 => 메모이제이션 = memoization => 답을 메모하겠다.

# 피보나치 수열 (메모)
d = {0:1, 1:1} # [1, 1] 피보나치 수열을 딕셔너리에 기록하겠다.
def fibo(idx):
    if idx in d: # d 라는 딕셔너리에 기록이 되어 있다면
        return d[idx] # 답을 return
    else: # 아직 d라는 딕셔너리에 기록이 되어 있지 않다.
        d[idx] = fibo(idx - 1) + fibo(idx - 2)
        return d[idx]

fibo(100)
fibo(100) # 위에서 구한 값을 출력 (이미 d에 기록해놨음)

# 함수를 선언할 때는
# 함수 이름을 잘 짓고
# 주석을 잘 달아야 된다.


