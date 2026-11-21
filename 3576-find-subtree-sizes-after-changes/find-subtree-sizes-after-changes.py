
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        previous = {}

        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()

            if exiting:
                if previous[node] == -1:
                    last.pop(s[node], None)
                else:
                    last[s[node]] = previous[node]
                continue

            previous[node] = last.get(s[node], -1)

            if previous[node] != -1:
                new_parent[node] = previous[node]

            last[s[node]] = node

            stack.append((node, True))

            for child in reversed(children[node]):
                stack.append((child, False))

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [1] * n
        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()

            if not exiting:
                stack.append((node, True))
                for child in new_children[node]:
                    stack.append((child, False))
            else:
                for child in new_children[node]:
                    answer[node] += answer[child]

        return answer
