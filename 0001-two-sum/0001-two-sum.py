class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the value and its index
        seen = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            # Calculate the complement that would sum with num to get the target
            complement = target - num
            
            # If the complement is already in the dictionary, return its index and the current index
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i
