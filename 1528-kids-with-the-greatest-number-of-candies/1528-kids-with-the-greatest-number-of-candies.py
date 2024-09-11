from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)  # Initialize result list with False
        m = max(candies)  # Find the maximum number of candies
        
        for i in range(len(candies)):
            # Check if current kid's candies + extraCandies is greater than or equal to max candies
            if candies[i] + extraCandies >= m:
                res[i] = True  # Mark this kid as True if the condition is met
        
        return res
