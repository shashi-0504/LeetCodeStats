1class Solution(object):
2    def diagonalPrime(self, nums):
3        def isprime(n):
4            for i in range(2,int(n**0.5)+1):
5                if n%i==0:
6                    return False
7            return True
8        l=[]
9        for i in range(len(nums)):
10            for j in range(len(nums)):
11                if i==j or i+j+1==len(nums):
12                    if isprime(nums[i][j]):
13                        l.append(nums[i][j])
14        if len(l)>=1 and max(l)>1:
15            return max(l)
16        else:
17            return 0
18        