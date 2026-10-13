
class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted([x * x for x in nums])

        ans = 0
        n = len(squares)

        for i in range(n):
            if i < (n + 1) // 2:
                ans += squares[n - 1 - i]
            else:
                ans -= squares[i - ((n + 1) // 2)]

        return ans
