class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = []
        f_cnt = 0
        for i in nums:
            cnt = 0
            while i > 0:
                r = i % 10
                cnt += 1
                i = i // 10
            res.append(cnt)
        
        for i in res:
            if i % 2 == 0:
                f_cnt += 1
        return f_cnt

        

        