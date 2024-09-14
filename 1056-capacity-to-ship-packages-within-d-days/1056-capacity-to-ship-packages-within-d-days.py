class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(capacity):
            days_d = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days_d += 1
                    if days_d > days:
                        return False
            return True
                    

        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        