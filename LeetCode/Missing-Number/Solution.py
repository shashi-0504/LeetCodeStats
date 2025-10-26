class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=sum(nums)
        return ((n*(n+1))//2)-s
        