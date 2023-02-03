list_a = [i for i in range(1, 30 + 1)] # 속도 더 빠름
# list_a = list(range(1, 30 + 1))
# 또는 for문 쓰기

# 없애는 방법 1 (remove는 왼쪽부터 쭉 찾아가기 때문에)
# 자주 쓰면 느려질 수도 있음
for _ in range(28):
    a = input()
    list_a.remove(int(a))


# 방법 2
# 딕셔너리 => 키-값 쌍으로 저장하는 자료구조
# d = {i:False for i in range(1, 30 + 1)}
# print(d)
#
# for _ in range(28): # 28번 입력받아서, 2개 빼고 다 True
#     a = int(input()) # 28번 입력되는 것
#     d[a] = True # 입력된 것은 True 바뀜
# print(d) # 2개만 False인 상태
#
# # 1 ~ 30까지의 KEY가 무슨 값을 가지는지 딕셔너리에 확인
# for i in range(1, 30 + 1): # 1 ~ 30까지 다 확인해보는 과정
#     if d[i] == False: # 아직도 False 입력되지 않았다는 뜻
#         print(i) # 무조건 end='\n' 정해져 있어서 줄바꿈

# 리스트로 하는 방법
checked = [False for i in range(30 + 1)] # True,True... 31개가 들어감
checked[0] = True # 안 쓰는 거니까 False로 답에 포함되지 않게ㅔ

for i in range(28):
    a = int(input()) # 1..30 랜덤 숫자
    checked[a] = True

answer = []
for i in range(1, 30 + 1):
    if checked[i] == False:
        answer.append(i)

# 만약에 내림차순으로 답을 제출해야 되면
# range를 역순으로 진행시키거나
# 답 list에 답을 넣은 다음, sort 함수로 내림차순으로 정렬
# answer.sort(reverse=True)