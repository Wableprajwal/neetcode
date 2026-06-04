class Solution:
    def isValid(self, s: str) -> bool:
        dp = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for c in s:
            if c in dp and stack:
                if stack[-1] != dp[c]: return False
                else: stack.pop()
            else:
                stack.append(c)
        return True if not stack else False
