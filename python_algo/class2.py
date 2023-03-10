l = [1,2,3]
for num in l: # N번
    print(num)
#  O(N)이 걸리는 코드다.

# Big-O
# 코드가 작동하는데 걸리는 시간을 나타내는 기호

for num in l:
    for num in l:
        pass # N^2
# O(N^2)
# O(N) <- 좋음
# O(NlogN) <- 거의 대부분의 상황에서 이게 엄청 빠른 편
# O(N^2)<- 여기부터는 조심
# 천만번을 대충 1초로 치는데, 그걸 고려해야된다.
# O(N^3) <- N=10일때 처럼 N이 작으면, N 세제곱도 그렇게 크지않다.
# 그래서 무작정 Big-O가 좋지 않아보인다고 안 쓰면 안 된다.