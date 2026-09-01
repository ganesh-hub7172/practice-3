from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and all litter positions
        start = None
        litter = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        # Give every litter cell a bit number
        litter_id = {}
        for i, pos in enumerate(litter):
            litter_id[pos] = i

        # All litter collected
        target = (1 << k) - 1

        # BFS: (row, col, energy, mask)
        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            for _ in range(len(queue)):
                r, c, e, mask = queue.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1