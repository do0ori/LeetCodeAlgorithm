class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            needed_hours = 0
            for pile in piles:
                needed_hours += -(-pile // mid)
                if needed_hours > h:
                    break
            
            if needed_hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left