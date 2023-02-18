class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1  #이 문장이 이해가 안됨
            #만약 for문을 사용해서 for i in range(len(s)-1)
            #     s[i] = s[-i-1]이러한 형식일때는 이해가 가능한데
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1