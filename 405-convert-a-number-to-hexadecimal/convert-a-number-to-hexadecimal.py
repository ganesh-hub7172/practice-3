class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32

        digits = "0123456789abcdef"
        ans = ""

        while num:
            ans = digits[num & 15] + ans
            num >>= 4

        return ans