#11720
n = int(input())
# for i in range(n): -> 여러줄 입력받기
#     a = input().spilt()
#     a = int(a)
#     a+=a
#     print(a)

# 한줄 입력
# input() = 문자열 한줄 (숫자처럼 생긴 문자열) '54321'
a = list(input()) # 한글자 한글자씩 쪼개서 리스트에 담는다. ['5', '4', '3', '2', '1']
a = map(int, a) # 문자열 -> int로 변환
# map, filter -> 변환 후에 바로 리스트가 되는 게 아니라, map/filter object
print(sum(a)) # 어떤 데이터들을 담고 있는 자료구조를 전달해주면 됨 (iterable)


#split 안되고 긴 숫자라 어떻게 나누어야 할 지 모르겠다