class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        length = len(nums)

        for i in range(length - k + 1):
            frame = nums[i:i+k]
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        
        return min_diff
