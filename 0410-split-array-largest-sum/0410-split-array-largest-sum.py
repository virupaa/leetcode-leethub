class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isSplit(capacity):
            total = 0
            days = 1
            for num in nums:
                total += num
                if total > capacity:
                    total = num
                    days += 1
                    if days > k:
                        return False
            return True





        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if isSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left

        