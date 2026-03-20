1class Solution(object):
2    def rotate(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: None Do not return anything, modify matrix in-place instead.
6        """
7        n=len(matrix)
8        for i in range(n):
9            for j in range(i,n):
10                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
11        for i in range(n):
12            matrix[i].reverse()
13        