class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = [amount+1]*(amount+1)
        total[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0:
                    total[a] = min(total[a], 1 + total[a-c])
        return total[amount] if total[amount] != amount+1 else -1