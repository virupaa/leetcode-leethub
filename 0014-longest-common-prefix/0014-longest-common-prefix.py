class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         print("S",s[i])
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return s[:i]


        