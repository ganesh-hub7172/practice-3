class Solution:
    def missingInteger(self, nums):
        # Find sum of longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find smallest missing integer >= total
        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total