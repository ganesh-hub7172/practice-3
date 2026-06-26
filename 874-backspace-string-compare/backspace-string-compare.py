class Solution:
    def backspaceCompare(self, s, t):
        def build(string):
            stack = []

            for ch in string:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)