class Solution:
    def minSwaps(self, data: List[int]) -> int:
        countOnes = data.count(1)
        curZero = 0
        n = len(data)

        for i in range(countOnes):
            if data[i] == 0:
                curZero += 1
        res = curZero

        for i in range(countOnes, n):
            if data[i] == 0:
                curZero += 1
            if data[i-countOnes] == 0:
                curZero -= 1
            
            res = min(res, curZero)
        return res


        

        