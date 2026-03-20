1class Solution(object):
2    def flipAndInvertImage(self, image):
3        """
4        :type image: List[List[int]]
5        :rtype: List[List[int]]
6        """
7        n=len(image)
8        for i in image:
9            i.reverse()
10        for i in range(n):
11            for j in range(n):
12                if image[i][j]==0:
13                    image[i][j]=1
14                else:
15                    image[i][j]=0
16        return image
17
18
19        