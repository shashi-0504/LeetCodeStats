1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s=0
4        for i in digits:
5            s= int("".join(map(str, digits)))
6        s=s+1
7        l=[]
8        while s:
9            r=s%10
10            l.append(r)
11            s//=10
12        return l[::-1]
13        