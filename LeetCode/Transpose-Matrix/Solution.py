1class Solution(object):
2    def transpose(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: List[List[int]]
6        """
7        r, c = len(matrix), len(matrix[0])
8        t=[[0]*r for _ in range(c)]
9        for i in range(len(matrix)):
10            for j in range(len(matrix[0])):
11                t[j][i]=matrix[i][j]
12        return t