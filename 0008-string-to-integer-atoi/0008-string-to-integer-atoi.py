class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespaces

        if not s:
            return 0

        i = 0
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1

        parsed = 0
        
        while i < len(s):
            curr = s[i]
            if not curr.isdigit():
                break
            parsed = parsed * 10 + int(curr)
            i += 1

        parsed *= sign
        
        # Clamp the value to 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if parsed > INT_MAX:
            return INT_MAX
        elif parsed < INT_MIN:
            return INT_MIN
        else:
            return parsed
