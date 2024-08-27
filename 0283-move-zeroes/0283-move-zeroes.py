class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        L = 0
        R = 1
        while R < n:
            if nums[L] != 0:
                L+=1
                R+=1
            elif nums[R] == 0:
                R+=1
            else:
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
            


        