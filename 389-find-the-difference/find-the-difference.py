class Solution:
    def findTheDifference(self, s, t):
        ans = 0

        for c in s:
            ans ^= ord(c)

        for c in t:
            ans ^= ord(c)

        return chr(ans)