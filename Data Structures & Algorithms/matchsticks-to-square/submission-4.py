class Solution:
    def makesquare(self, match: List[int]) -> bool:
        length = sum(match)//4
        if sum(match)/4 != length : return False
        sides = [0]*4
        match.sort(reverse=True)
        def dfs(i):
            if i == len(match): return True
            for j in range(4):
                if sides[j] + match[i] <= length:
                    sides[j] += match[i]
                    if dfs(i+1): return True
                    sides[j] -= match[i]
            return False
        return dfs(0)