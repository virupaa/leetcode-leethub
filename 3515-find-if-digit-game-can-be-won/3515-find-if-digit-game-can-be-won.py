from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0
        other_sum = 0
        
        for num in nums:
            if 1 <= num <= 9:
                single_digit_sum += num
            elif 10 <= num <= 99:
                double_digit_sum += num
            else:
                other_sum += num
        
        # Alice can choose either all single-digit numbers or all double-digit numbers
        # Check if the sum of single-digit numbers is greater than the sum of the rest
        if single_digit_sum > double_digit_sum + other_sum:
            return True
        
        # Check if the sum of double-digit numbers is greater than the sum of the rest
        if double_digit_sum > single_digit_sum + other_sum:
            return True
        
        return False


