class Solution:
    def isValid(self, s: str) -> bool:
        if s[0]==']' or s[0]== '}' or s[0]==')':
            return False
        st=[]
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if not st:
                    return False
                if (i==")" and st[-1]=="(") or (i=="]" and st[-1]=="[") or ( i=="}" and st[-1]=="{"):
                        st.pop()
                else:
                    return False
        if st:
            return False
        return True