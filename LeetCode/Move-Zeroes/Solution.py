1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        for i in nums:
7            if i==0:
8                nums.remove(i)
9                nums.append(0)