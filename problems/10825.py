n = int(input())
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


list = [] # 학생이라는 객체들을 담았음
for i in range(n):
    name, k, e, m = input().split()
    s = Student(name,int(k),int(e),int(m))
    list.append(s)


list.sort(key=lambda s: (-s.korean, s.english, -s.math, s.name)) # 정렬 함수
# 양수로 적으면. 오름차순으로 정렬하겠다는 얘기. 즉, 증가하는 순서
# 음수로 바꿔주면 내림차순으로 정렬하겠다는 얘기
# sort 함수 안에 위 형식으로 기준만 정해주면 알아서 다 정렬해줌.
print('\n'.join([s.name for s in list]))
