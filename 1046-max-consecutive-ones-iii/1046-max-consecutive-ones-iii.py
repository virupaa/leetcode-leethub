class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        n = len(nums)
        l = 0
        num_z = 0
        for i in range(n):
            if nums[i] == 0:
                num_z += 1
            while num_z > k:
                if nums[l] == 0:
                    num_z -= 1
                l += 1
            w = i - l + 1
            max_w = max(max_w, w)
        return max_w
                
        