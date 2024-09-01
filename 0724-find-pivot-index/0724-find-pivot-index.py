class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        sum_n = sum(nums)
        for i in range(len(nums)):
            rightSum = sum_n - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
        