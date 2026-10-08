class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0

        for ch in s:
            if ch == '(':
                # If balance > 0, this is not an outer '('
                if balance > 0:
                    result.append(ch)
                balance += 1

            else:  # ch == ')'
                balance -= 1

                # If balance > 0, this is not an outer ')'
                if balance > 0:
                    result.append(ch)

        return ''.join(result)