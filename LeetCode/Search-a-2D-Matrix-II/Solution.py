1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        m=len(matrix)
9        n=len(matrix[0])
10        for i in range(m):
11            for j in range(n):
12                if(matrix[i][j]==target):
13                    return True
14                    break
15        return False
16        