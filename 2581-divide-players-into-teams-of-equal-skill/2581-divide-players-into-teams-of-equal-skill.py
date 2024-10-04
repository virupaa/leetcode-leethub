class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_ = sum(skill)
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        if sum_ % (n//2) != 0:
            return -1
        skill.sort()
        score = skill[0] + skill[-1]
        pairs = []
        result = 0
        for i in range(n // 2):
            l, r = skill[i], skill[n - 1 - i]
            if l + r != score:
                return -1
            result += l * r
        return result

with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(Solution().dividePlayers(nums),file=f)
exit(0)