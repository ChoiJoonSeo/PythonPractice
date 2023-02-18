from collections import defaultdict

#딕셔너리 생성 방법
d = dict() # 처음에 아무값도 안 가짐
d2 = {"최준서":24, "박동현":28, 24:"최준서"} # 값을 가지고 시작
s = {} # 집합, set (딕셔너리 아님)

age = d2["최준서"]
name = d2[24]
print(name)

d2["학생"] = ["최준서", "철수"]
me = d2["학생"][0]
# del d2["학생"] # 키없애기

print(d2["학생"])
print(d2.get("학생"))
print(d2.get("sdfsdfsdfsd")) # 없는 키도 Error 안 남

# defaultdict
dd = defaultdict(list) # 전달해준 데이터 타입의 가장 기초상태를 돌려줌 (등록 안 했다면)

dd[24].append(2) # dd가 [ ]리스트를 생성하고, 거기에 2를 넣음
print(dd[24]) # [2]

# 아직 24라는 key를 등록하지 않았지만,
# defaultdict 자동으로 등록하고 값을 0으로 설정했다.

# in -> 딕셔너리에 key가 있냐를 확인
print("최준서" in d2)

# for문 -> key 순서대로 탐색
print()
for key in d2:
    print(key, d2[key]) # 키 - 값

print()
for key, value in d2.items():
    print(key, value)