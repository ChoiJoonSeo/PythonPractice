from sys import stdin # 콕 찍어서 사용할 것만 언급
from collections import defaultdict, Counter, deque
import heapq
from copy import deepcopy
import math
from itertools import combinations, permutations
from bisect import bisect_left, bisect_right


input = stdin.readline().rstrip # 엔터도 받음
# sys.stdin.readlines() 최대 1000줄까지 입력받아서 리스트로 만듦
print(input())
# sys.exit() 더이상 코드를 실행할 필요가 없을 때 부르면 된다.


# collections

# defaultdict
d = defaultdict(int) # 내가 기본값으로 사용할 데이터를 설정
# 기본값을 갖는 딕셔너리
# 어떤 기본값을 쓰고 싶은지 데이터 타입을 전달해주면 된다.

print(d[1]) # 바로 0이라는 값을 출력

# Counter
l = [1, 2, 3, 1, 2, 2]
counter = Counter(l)
# {1=2, 2=3, 3=1}
# 딕셔너리랑 똑같음
counter.items() # 딕셔너리 기능을 완전히 똑같이 사용할 수 있음
counter[4] = 1
s = 'aabbccabc'
counter_s = Counter(s) # 문자 안에 어떤 문자가 몇개 있는지도 알 수 있다.

d = defaultdict(dict)
a = '아야아'
counter_a = Counter(a)
print(counter_a)

d[1][1] = 2
print(d[1])
# d라는 defaultdict에 1이라는 key로 접근
# 근데 값이 빈 딕셔너리고, 거기서 1이라는 key에 2라는 값을 등록

# deque(덱) 자료구조
# 스택 <- 위로 쌓이는 자료구조. 뺄때도 위에꺼부터 뺀다.
# Queue(큐) <- 좌, 우로 넣고 빼는 자료구조
l = [1, 2, 3, 4, 5]
del l[1] # 2를 없애면, 3, 4, 5가 한칸씩 앞으로 당겨짐
# 리스트 앞에 있는 것들을 없애면 뒤에 애들이 앞으로 밀려오기 때문에
# 점점 느려짐

# 큐 (deque)
q = deque() # 큐를 생성했음
q.append(1)
q.append(2)
q.append(3)
print(q.pop()) # 3을 return하면서 큐에서 제거된다.
print(q.popleft()) # 1을 return하면서 큐에서 제거
print(q.popleft()) # 남은 것은 2밖에 없음

# 스택 (리스트로 만들 수 있음)
stack = []
stack.append(1)
stack.append(2)
stack.pop()
# 리스트를 선언하고, append랑 pop만 쓰면 그게 stack이다.


# heapq (트리)
# 데이터를 뺄 때, 우선순위를 설정할 수 있음
# 파이썬의 heapq 기본적으로 최소 힙인데,
# heappop을 써서 데이터를 빼면 리스트에서 최소값을 빼준다.
heap = [1, 1, 2, 3, 2, 2, 1, 5]
heapq.heapify(heap) # 힙화
heapq.heappush(heap, 0) # 규칙을 지키면서 0을 넣겠다.
print(heapq.heappop(heap)) # 0이 나옴
# 만약에 최대값을 빼고 싶다면
# 넣을 때 강제로 마이너스를 붙여서 음수로 바꿔서 넣어야 된다.
# 그러면 heappop을 쓰면 마이너스 붙은 최대값이 나온다.


# copy (복사)
c = [1, 2, 3]
cc = c[:] # 값만 복사

cc[0] = 10
print(c)

c2 = [[1, 2], [3, 4]]
cc2 = c2[:] # 제일 바깥에 있는 것만 값을 복사했고
# 안쪽에 있는 것들은 그대로 가져온 것..

cc3 = deepcopy(c2) # 값을 새롭게 다 복사

cc2[0][0] = 100
print(c2) # c2도 변했음

cc3[0][0] = 1000
print(c2) # cc3를 바꿨지만 영향 없음

# 수학 관련 라이브러리
math.ceil(1.1) # 올림 -> 2
math.floor(1.2) # 내림 -> 1
round(1.5) # 반올림 (기본)
math.gcd(2, 8) # 최대공약수

# 조합과 순열
ll = [1, 2, 3, 4]
print(list(combinations(ll, 2))) # 조합 많이 씀
print(list(permutations(ll, 2)))

# 이진 탐색
b = [1, 2, 2, 3]
# bisect는 이진탐색 했을 때 들어갈 수 있는 위치(인덱스)를 돌려준다.
print(bisect_left(b, 2)) # lower bound
print(bisect_right(b, 2)) # upper bound
