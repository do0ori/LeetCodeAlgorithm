class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            eating_h = 0
            for pile in piles:
                eating_h += -(-pile // mid)
            
            if eating_h <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left