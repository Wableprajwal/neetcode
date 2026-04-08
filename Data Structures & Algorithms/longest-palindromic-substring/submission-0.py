class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l,r):
            nonlocal longest
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > longest:
                    longest = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
    
        res = ""
        longest = 0
        for i in range(len(s)):
            pal(i,i)
            pal(i,i+1)
        return res