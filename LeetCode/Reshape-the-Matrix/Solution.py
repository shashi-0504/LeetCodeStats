class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        f=[]
        n=[]
        for i in mat:
            for j in i:
                f.append(j)
        if r*c!=len(f):
            return mat
        else:
            for i in range(r):
                n.append(f[i*c:i*c+c])
            return n


                


        