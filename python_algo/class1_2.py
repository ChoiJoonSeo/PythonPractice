from collections import Counter
import re # 정규식 <- Regex

# 문자열은 모듈 (import 해서 사용하는 것) 많이 아는 게 갑
# 하면 할수록 실력이 늘어가는 영역
# 모듈 많이 쓰면 너무 쉽게 풀리는 문제가 많다.
# 근데 어떤 모듈 쓸지 모르겠으면 노가다로라도 풀자.
# (리스트 내포 같은 거 기억 안 나고 하면 for문을 깡으로 써서)
# 문자열 <- 센스가 거의 반


# 문자열 함수
# type('문자') -> 'str' 타입
# upper() -> 대문자, lower() -> 소문자
# isupper(), islower() <- 대문자인지 소문자인지 확인
# 특정 문제에서는 대문자와 소문자를 구분하지 않는다고 설명을 함. 그러면 다 소문자로 바꾸거나 대문자로 바꿔줘야됨
print('my name is pdh'.upper())
print('MY NAME IS PDH'.lower())
print('m' == 'M'.lower()) # 둘이 같은 문자로 취급되도록 한쪽을 다른 쪽에 맞게 바꿔줘야 됨.
# 이 문자열이 숫자 형태인지 그냥 알파벳인지 확인하는 함수
# isdigit <- 숫자인지 확인 isalpha <- 알파벳 isalnum <- 알파벳 혹은 숫자인지 확인
print('m'.isdigit())
print('1'.isdigit())
print('masmdfmasdmfsamdfm 1'.isdigit()) # 싹다 숫자 문자열인지 확인
print('masdfasdfasdf1'.isalnum()) # 싹다 숫자 혹은 알파벳인지 확인


# 슬라이싱
s = 'CJSPDH'
s[0] # C
s[1:2 + 1] # JS
s[::-1] # 뒤집기 <- 중요
s[::-2] # 거꾸로 S부터 시작해서 간격은 2로
s[:] # 완전 복사하는 것 <- 중요
s[0:3:2] # 처음부터 시작해서 간격은 2
s[0:2] + s[3:] # CJ + PDH -> CJPDH (S를 제거)

# 문자를 정렬을 하고 싶을 때
l = [3, 2, 1]
sorted(l) # 원본에는 영향이 없음. l에 아무일도 안 일어남.. 그래서 받아주는 변수가 있어야 된다.
print(*l)

l.sort() # 리스트에는 sort가 있음
print(*l)

a = 'cba'
sorted_a = sorted(a) # a에는 영향이 없지만, a를 정렬한 문자열을 리턴
# sorted에 문자열을 전달하면, 쪼개서 정렬하고 리스트로 돌려줌.
print(''.join(sorted_a)) # 리스트를 한 문자열로 바꿈
# 문자열을 정렬하고 싶다면, sorted를 쓴 다음 join으로 다시 합쳐줘야됨.

# Counter <- 문자열 안에 어떤 문자가 몇개 있는지 쉽게 확인 가능
counter = Counter([1, 2, 3]) # 딕셔너리 형태로 준다..
s_counter = Counter('asdvasdvsvzsdvdsvsdzzvsd')
print(s_counter.most_common(2)) # 2등까지 알려준다.

# 정규식 <- 너가 원하는 형태의 문자를 찾고 싶을 때 사용
# re 모듈을 import
'[0-9a-Z가-힣]' # <- 숫자 혹은 알파벳 혹은 한글 1글자를 필터링하겠다.

'asdnvklasdㅍㅁㄴㅇ퓌121389128923.,  .ㅁㄴㅇ,ㄹ.ㅁ ㅐ2 3햐가ㅣㅠ리ㅏㄴ유뮤ㅏㅣ'
print(re.sub('[^0-9A-zㄱ-ㅎ가-힣]', '', 'asdnvklasdㅍㅁㄴㅇ퓌121389128923.,  .ㅁㄴㅇ,ㄹ.ㅁ ㅐ2 3햐가ㅣㅠ리ㅏㄴ유뮤ㅏㅣ'))
# 간편하게 내가 없애고 싶은 문자들을 제거할 수 있다.

# sub <- 정규식에 해당하는 문자들을 특정 문자로 바꾸겠다.
# sub(정규식 패턴, 바꿀 문자, 전체 문자열)
print(re.sub('[ㄱ-ㅎ]', '한글', 'ㄱㄴㄷㄹㅁㅂㅅabsdcasdc'))

# 기능이 되게 많지만, 필요할 때마다 찾아가면서 기억해두는 게 낫다.
regex = re.compile('[ㄱ-ㅎ]') # 정규식을 저장해두고 계속 재사용
regex.sub('한글', 'ㄱㅁㄴㅇㅁㄴㅇㅍㅁㅁㄴㅍㄴㅁㅇ')
