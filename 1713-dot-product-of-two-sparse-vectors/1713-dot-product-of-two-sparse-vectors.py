class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: x for i, x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(self.d[key]*vec.d.get(key, 0) for key in self.d)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)