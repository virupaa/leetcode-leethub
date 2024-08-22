class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)
        a = list(bin_num[2:])
        b = []
        for i in a:
            if i == '0':
                i = '1'
                b.append(i)
            else:
                i = '0'
                b.append(i)
        return int(''.join(b),2)
        