1class Solution(object):
2    def maximalRectangle(self, matrix):
3        if not matrix or not matrix[0]:
4            return 0
5        n = len(matrix[0])
6        height = [0] * (n + 1)
7        ans = 0
8        for row in matrix:
9            for i in xrange(n):
10                height[i] = height[i] + 1 if row[i] == '1' else 0
11            stack = [-1]
12            for i in xrange(n + 1):
13                while height[i] < height[stack[-1]]:
14                    h = height[stack.pop()]
15                    w = i - 1 - stack[-1]
16                    ans = max(ans, h * w)
17                stack.append(i)
18        return ans
19
20        