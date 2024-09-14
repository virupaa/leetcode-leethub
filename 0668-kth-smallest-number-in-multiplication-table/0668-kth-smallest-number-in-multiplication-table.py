class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def feasible(num):
            count = 0
            for i in range(1,m+1):
                val = min(num // i, n)
                if val == 0:
                    break
                count += val
            return count >= k
        
        left, right = 1, m*n
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

        


