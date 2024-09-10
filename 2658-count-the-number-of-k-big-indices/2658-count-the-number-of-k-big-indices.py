class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        maxHeap = []
        count = 0

        leftCondMet = [False] * len(nums)

        for i, n in enumerate(nums):
            if len(maxHeap) == k and -maxHeap[0] < n:
                leftCondMet[i] = True
            heappush(maxHeap, -n)
            if len(maxHeap) > k:
                heappop(maxHeap)
            
        
        maxHeap = []
        for i, n in reversed(list(enumerate(nums))):
            if len(maxHeap) == k and -maxHeap[0] < n and leftCondMet[i]:
                count += 1
            heappush(maxHeap, -n)
            if len(maxHeap) > k:
                heappop(maxHeap)
        return count

        


        