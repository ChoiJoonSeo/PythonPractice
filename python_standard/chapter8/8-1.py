def plus(x, y): # 추상화의 대표적인 예시 -> 메소드(함수)
    return x + y
# 추상화를 잘 하는게 중요하다 (사용자가 쉽게 쓸 수 있도록 만드는 것)

# 상속: 부모의 속성 및 함수를 모두 활용할 수 있게 되는 것
# 상속을 왜 하는가? 중복된 코드를 제거하고 공통점을 묶어서 재사용성을 높인다.
# 상속이 너무 깊어지면 좋지않다. 적당히 써야 자기 자신도 헷갈리지 않는다.
# 자식이 여러 부모를 가질 수 있긴 하지만, 하나의 부모만 가지는 게 좋다. (Java는 애초에 하나의 부모만 가질 수 있다.)
class Person: # 부모
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self): # 객체가 사용할 함수
        print(f'저는 {self.name}이고, 나이는 {self.age} 살 입니다.')

# 클래스
# 붕어빵 틀(설계 도면) <-> 붕어빵(객체)
# 자식 <- 부모의 특성 모두 물려받음.
class Student(Person): # 클래스의 이름 정의
    count = 0 # 공용 변수를 정의할 수 있다.

    # 생성자 <- 객체가 생성될 때 필요한 데이터를 전달받으면서 뭔가를 하는 함수
    def __init__(self, name, age, major): # 한 객체에서 무조건 딱 한번만 실행되는 함수
        super().__init__(name, age) # 부모의 생성자 호출. 부모 = super
        self.major = major
        Student.count += 1

    # 소멸자 -> 필수는 아니고, 객체가 메모리에서 제거될 때 하고 싶은 게 있으면 선언하면 됨.
    def __del__(self): # 메모리에서 제거될 때 실행되는 함수
        print(f'{self.name}이 제거되었습니다.')

    # 클래스로 만든 객체를 바로 편하게 출력하고 싶으면, __str__ 정의해주면 된다.
    def __str__(self): # 문자열처럼 사용될 부분을 정의해주는 것
        return self.name

    # getter
    @property # 파이썬: 데코레이터 (아래 코드의 의미를 나타내는 코드)
    def age(self):
        return self.__age

    # setter
    @age.setter # 값을 바꿀 수 있게 만드는 것. 근데 private으로 설정했다는 것 자체가 값을 바꾸기 싫어서 하는 것.
    # 그래서 private에 이걸 선언할 경우가 거의 없다고 봐야됨.
    def age(self, age):
        self.__age = age

    # 비교함수들은 여러번 쓸 때 재사용성이 높아지기 때문에, 정의하면 좋지만. 한번 쓸거면 굳이 안 해도 된다.
    # __eq__: 같다의 기준을 정함
    def __eq__(self, other): # 우리가 세운 기준에 맞게 같은지 아닌지가 결정된다.
        return self.name == other.name and self.age == other.age # 이름과 나이가 같으면 같다. 라고 기준을 세우는 것

    # __gt__: greater than
    def __gt__(self, other):
        return self.age > other.age

    # __ge__: greater equal than 이상 (크거나 같으면)
    # __lt__: less than 미만
    # __le__: less equal than
    # __ne__: not equal 같지 않다에 대한 기준


Student('KKK', 20, 'CS') # 가비지 컬렉터가 청소함 (변수에 저장되지 않았고 앞으로 사용될 일이 없다고 판단되기 때문에)
print('방금 변수에 저장없이 Student 생성했음')
s1 = Student('CJS', 24, 'CS') # 객체 생성
s2 = Student('PDH', 28, 'CS')

s1.name = '최준서' # 값을 바꿀 수 있음
s1.introduce()
s1.__gender = '남자' # 밖에서는 언더바 두개를 붙여서 추가를 해도 접근이 가능하다.
s1.age = 20202 # setter를 선언해줬기 때문에 private 변수에도 값을 변경할 수 있다.

print(s1)
print(s1 == s2) # 기본적으로 주소값을 비교. 그런데 __eq__를 정의해주면 우리가 설정한 기준에 맞게 비교함.
print(s2 > s1)

# 어떤 객체가 특정 Class인지 확인할 때 쓰는 함수
if isinstance(s1, Student): # type(s1) == Student
    print('s1은 Student 객체입니다.')


# 끝줄에 도달하면 지금까지 선언한 변수나 자료구조를 알아서 다 정리함...
# s1이나 s2 라는 변수도 제거가 됨 (메모리에서 자동으로)