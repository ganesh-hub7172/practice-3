class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        # Flatten the matrix
        flat = []
        for row in mat:
            flat.extend(row)

        # Build the reshaped matrix
        ans = []
        for i in range(0, len(flat), c):
            ans.append(flat[i:i + c])

        return ans