1class Solution(object):
2    def nextGreatestLetter(self, letters, target):
3        """
4        :type letters: List[str]
5        :type target: str
6        :rtype: str
7        """
8        for i in letters:
9            if i>target:
10                return i
11        return letters[0]
12        