class Solution:
    def isPalindrome(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]