1class Solution(object):
2    def diagonalSum(self, mat):
3        """
4        :type mat: List[List[int]]
5        :rtype: int
6        """
7        n=len(mat)
8        k=0
9        for i in range(n):
10            for j in range(n):
11                if(i==j or i+j+1==n):
12                    k+=mat[i][j]
13        return k
14
15        