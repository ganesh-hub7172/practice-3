class Solution:
    def shortestBeautifulSubstring(self, s, k):
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""
        min_len = float('inf')

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            substring = s[left:right + 1]
            length = len(substring)

            if length < min_len:
                min_len = length
                ans = substring
            elif length == min_len and substring < ans:
                ans = substring

        return ans