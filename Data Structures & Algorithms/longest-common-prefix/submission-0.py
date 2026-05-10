class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]: return res
            res += strs[0][i]
        return res