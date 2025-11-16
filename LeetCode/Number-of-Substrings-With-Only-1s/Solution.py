class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count1 = 0  # current streak of '1's
        ans = 0     # total substrings

        for c in s:
            if c == '1':
                count1 += 1          # extend streak
                ans = (ans + count1) % MOD  # add new substrings
            else:
                count1 = 0           # reset streak

        return ans
