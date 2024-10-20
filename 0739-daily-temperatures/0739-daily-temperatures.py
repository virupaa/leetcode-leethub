class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, index

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([n, i])
        return res

        