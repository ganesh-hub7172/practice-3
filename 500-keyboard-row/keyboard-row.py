class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = word.lower()

            if w[0] in row1:
                if all(ch in row1 for ch in w):
                    result.append(word)

            elif w[0] in row2:
                if all(ch in row2 for ch in w):
                    result.append(word)

            else:
                if all(ch in row3 for ch in w):
                    result.append(word)

        return result