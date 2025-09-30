class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        k=set(nums)
        for i in k:
            if nums.count(i)==1:
                l.append(i)
        return l
        