class Solution:
    def longestPalindrome(self, s: str) -> str:


#for i in range(len(s)):
#    if s[i] != s[-i-1]: #한 번이라도 다르면 끝이므로
#    else:
         # 이것 자체가 펠린드롬
 #중간에서부터 시작되어 앞뒤로 같을 때 펠린드롬이 늘어나는 코딩
 #len(s)가 짝수일때와 홀수 일떄 len(s)/2 와 len(s)//2 ->결국 len(s)//2
 #a = 0
 #for i in range(len(s)):
 #   s[len(s)//2-i] == s[len(s)//2+i]

 #   print(s[len(s)//2-i:len(s)//2+i+1])

           #생각해보니 이 코딩이 성립하려면 중심이 맞고 거기서부터 시작되야 가능

    #특정한 i 에서 위 아래가 맞을 때 늘어나는 방식으로 코딩
left , right #바뀔 수 있는 미지수가 되어야 함 for _ in range(len(s))
while s[left] == s[right]:
    left -= 1
    right += 1
    return s[left+1:right]
else:
    break


for i in range(len(s)):
for j in range(len(s)):
    s[i] == s[j]
    i -= 1
    j += 1

    return s[i+1:j]
#질문)이러한 for 문의 사용을 만드려면 어떻게 해야하나?

while left >= 0 and right <len(s) and s[left] == s[right]:
    left -= 1
    right += 1
return s[left+1:right]

#left >= 0 and right <len(s) 이게 left와 right에 들어갈 수 있는 조건인가?
# 0<=left,right<len(s) and left < right 이렇게  하고 시작하게 되면
# 이게 더 적게 찾는 것이 아닌가? (효율적이지 않나?)
# 아니면 조건 만족하는 자체가 작더라도 더 많이 돌면서 찾아야해서 더 시간이 걸리나?
#해당사항이 없을 경우
if len(s) < 2 or s == [::-1]

