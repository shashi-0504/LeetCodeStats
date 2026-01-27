1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        ans=[]
4        while matrix:
5            ans+=matrix.pop(0)
6            matrix=(list(zip(*matrix)))[::-1]
7        return ans