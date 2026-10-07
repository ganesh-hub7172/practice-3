from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        found = False
        result = []

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            # Once valid strings are found,
            # don't generate strings with more removals.
            if found:
                continue

            for i in range(len(current)):
                # Remove one character
                # Only parentheses need to be removed.
                if current[i] not in "()":
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result