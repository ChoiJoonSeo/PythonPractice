class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if num[i] + num[j] == target:
                    return[i,j]


    #2번쨰 방식이 이해가 힘듬 if문 부터
        for i, n in enumerate(nums): #튜플을 만들어줌
                                    # 따라서 구하고자 한다면 unpacking 필요
                                    # print(i,n)같은
            complement = target -n #보수(complement) 뺄셈연산을 위해 사용

            if complement in nums[i+1:]: #왜 i+1?
                return [nums.index(n), nums[i+1:].index(complement)+(i+1)]
 #3,4,번째 방식도 이해하기 힘듬
#5번은 len(nums)-1을 왜 하는지?

