# 구문 오류 syntax
# 0 = 9

# 런타임
l = [1,2]
d = dict()

try: # 혹시나 오류가 날 수도 있는 코드를 try 영역에 적음
    l[3] # IndexError
    d[354654] # KeyError
except IndexError: # Index Error만 잡고, try-except문을 벗어남
    print('인덱스 에러 발생')
except KeyError:
    print('키 에러')
except: # 모든 Error 다 잡는다.
    print('1')
    ...
else:
    print('에러 없었음')
finally: # try에서 에러가 나든 안 나든 무조건 실행한다.
    print('끝')

try: # try 혼자는 못 쓰고, except나 finally랑 같이 쓴다.
    print(2)
finally:
    print(2)

for i in range(5):
    print(i)
    break
else: # break가 안 걸리고 for문이 끝나면 오는 영역
    print('끝')

def func2():
    raise NotImplementedError
