class Solution:
    def decodeString(self, s):
        count_stack = []
        string_stack = []
        current = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                count_stack.append(num)
                string_stack.append(current)
                current = ""
                num = 0
            elif ch == "]":
                repeat = count_stack.pop()
                previous = string_stack.pop()
                current = previous + current * repeat
            else:
                current += ch

        return current