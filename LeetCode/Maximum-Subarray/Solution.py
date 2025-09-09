class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=0
        n=nums[0]
        for i in nums:
            if cs<0:
                cs=0
            cs+=i
            n=max(cs,n)
        return n