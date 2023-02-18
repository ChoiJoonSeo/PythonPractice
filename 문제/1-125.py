class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for l in s:
            if l.isalum():
                a.append(l.lower())
        while len(a) > 1:  #여기 밑에 for을 사용하면 이해 가능
                    # ->pop(0)은 제일 앞에것
            if a.pop(0) != a.pop():  #pop()에 아무것도 없을 때 왜 끝인지 모르겠다?
                return False
        # *질문)  이렇게 된것을 파이썬에서 실행은 어떻게 하는지

        #deque(양방향 넣고 뺴기 가능)를 사용한 풀이 2번은 이해가 가는데
#정규식 s = re.sub('[^a-z0-9]','',s) 이용 return s == s[::-1]3번 풀이도 이해

        test = [0, 0, 0, 1, 2, 3, 4, 5, 6]
        test1 = [0, 0, 0, 1, 2, 3, 4, 5, 6]

        for _dummy in test:
            if (_dummy == 0):
                test.pop()
        for _dummy in test1:
            if (_dummy == 0):
                test1.pop(0)

        print(test)
        print(test1)

        [0, 0, 0, 1, 2, 3]
        [0, 1, 2, 3, 4, 5, 6]
    #결과가 이렇게 나오는 것을 봐서 앞뒤 라는 것은 이해
    #그러나 test1에서 0이 남는 것이 이해가 안됨

    #알려준 다른 방식
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = list(s.lower())
        for i in range(len(a) - 1, -1, -1):  #len(a)-1 ~ 0까지의 의미
            if not a[i].isalnum():
                a.pop(i)
        return a == a[::-1]


    for i in range(5,-1.-1):
        print(i)