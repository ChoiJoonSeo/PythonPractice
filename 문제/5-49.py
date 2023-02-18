import collections
#자리를 바꾸어 같은 문자가 된다면 그것끼리 묶기
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)





        anagrams = [for word in strs re.sub('[^\w]','',anagrams)]
        #영문자 제외 다 제거 해서 anagrams에 대입/이게 가능?
        #딕셔너리에 이 기능이 없는 것인가?


        for word in strs:
            anagrams[''.join(sorted(word))].append(word) #이 줄이 이해가 잘 안됨
            #질문) *anagrams리스트 안에 join함수를 쓰면 어떻게 되는지 모르겠음
            #join함수가 앞에 있는 문자를 각각의 것에 들어가면서 하나의 문자열로 합치는 것인데
            #anagrams안에 들어가면 어떻게 될지?
            #sorted를 통해 키값을 지정하는 것이 맞는 것인가?
            
        return list(anagrams.values())#:값을 찾아서 리스트로 줌

#    strs = ['CBA', 'JOIN', 'Join', 'koO']
#    anagrams = {}  ->이것을 collections.defaultdict(list)로 바꾸니 가능

#   for word in strs:
#        anagrams[''.join(sorted(word))].append(word)  ->테스트가 안됨,
#잘문) 테스트가 안되는 원인?->이것을 collections.defaultdict(list)로 바꾸니 가능
#따라해서 결과가 나오는데 밑에 결과가 나옴 내가 원하는 것은 마지막 줄만
# [['eat']]
#[['eat', 'tea']]
#[['eat', 'tea'], ['tan']]
#[['eat', 'tea', 'ate'], ['tan']]
#[['eat', 'tea', 'ate'], ['tan', 'nat']]
#[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]