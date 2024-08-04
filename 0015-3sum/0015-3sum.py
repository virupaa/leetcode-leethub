from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for the first number

            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # Skip duplicate values for the second number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # Skip duplicate values for the third number
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
