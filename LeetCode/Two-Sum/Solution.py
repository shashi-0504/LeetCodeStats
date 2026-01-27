1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap={}
4        for i,n in enumerate(nums):
5            d=target-n
6            if d in hashmap:
7                return([hashmap[d],i])
8            hashmap[n]=i
9        
10            