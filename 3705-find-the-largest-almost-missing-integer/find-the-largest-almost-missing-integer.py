class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        count = {}

        # Check every subarray of size k
        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        # Find the largest number appearing in exactly one subarray
        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans