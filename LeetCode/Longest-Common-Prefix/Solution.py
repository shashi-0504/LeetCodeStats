class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        a=strs[0]
        b=strs[-1]
        c=0
        for i in range(len(a)):
            if a[i]==b[i]:
                c+=1
            else:
                break
        return a[:c]
        