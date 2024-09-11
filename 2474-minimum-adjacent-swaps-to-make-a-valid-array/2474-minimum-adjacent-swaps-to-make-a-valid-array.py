class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        smallest, largest, small_idx, large_idx = math.inf, -math.inf, 0, 0

        for i, n in enumerate(nums):
            if n < smallest:
                smallest = n
                small_idx = i
            if n >= largest:
                largest = n
                large_idx = i
        N = len(nums) - 1
        res = small_idx + (N - large_idx)

        return res - 1 if small_idx > large_idx else res
            

        