class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        for _ in range(k):
            res = -heapq.heappop(maxHeap)
           

        return res