class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l, r = 0, 1 #l=buy, r=sell
        maxp = 0

        while r < len(nums):
            if nums[l] < nums[r]:
                profit = nums[r] - nums[l]
                maxp = max(profit, maxp)
            else:
                l = r
            r += 1
        return maxp
       
        