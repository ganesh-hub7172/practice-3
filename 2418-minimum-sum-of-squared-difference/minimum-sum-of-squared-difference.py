class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        if k == 0:
            return sum(x * x for x in diff)

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(0, x - mid) for x in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        ans = 0
        operations = 0

        for x in diff:
            if x > level:
                ans += level * level
                operations += x - level
            else:
                ans += x * x

        # Use any remaining operations to reduce values at the threshold.
        remaining = k - operations
        ans -= remaining * (2 * level - 1)

        return ans
