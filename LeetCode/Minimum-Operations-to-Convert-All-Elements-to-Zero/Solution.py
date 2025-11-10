seen = [0] * 100001      # Boolean array: has value been seen?
stk = [0] * len(nums)    # Stack to maintain increasing sequence  
t = 0                     # Stack top pointer (current size)
res = 0                   # Result: count of operations needed