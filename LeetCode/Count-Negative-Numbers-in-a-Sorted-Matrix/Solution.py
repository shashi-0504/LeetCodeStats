1class Solution(object):
2    def countNegatives(self, grid):
3        """
4        :type grid: List[List[int]]
5        :rtype: int
6        """
7        c=0
8        for i in grid:
9            for j in i:
10                if j<0:
11                    c+=1
12
13        return c
14        