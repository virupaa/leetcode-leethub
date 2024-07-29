class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dict_m = collections.Counter()

        def fun(nums):
            for x in set(nums):
                dict_m[x] += 1
        
        fun(nums1)
        fun(nums2)
        fun(nums3)

        return list(x for x in dict_m.keys() if dict_m[x] >= 2)




        return [1,2,3]


        