from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1
            dp[tuple(count)].append(s)

        return list(dp.values())