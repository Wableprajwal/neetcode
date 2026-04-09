class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0: return False
        count = Counter(hand)
        hand.sort()
        for n in hand:
            if count[n]:
                for i in range(n,n+groupSize):
                    if i not in count: return False
                    count[i] -=1
        return True