1class Solution(object):
2    def transpose(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: List[List[int]]
6        """
7        l=[list(i) for i in zip(*matrix)]
8        return l