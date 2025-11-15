class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        map = {} # map for next greater element
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num) 
        for i in xrange(len(nums1)): 
            nums1[i] = map.get(nums1[i], -1)
        return nums1