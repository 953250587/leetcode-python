"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.



Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6


Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        456 ms
        """
        import heapq
        final, m, n, si, sj = 0, len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    final |= 1 << ord(grid[i][j]) - ord("a")
                elif grid[i][j] == "@":
                    si, sj = i, j
        q, memo = [(0, si, sj, 0)], set()
        while q:
            moves, i, j, state = heapq.heappop(q)
            if state == final: return moves
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                    if grid[x][y].isupper() and not state & 1 << (ord(grid[x][y].lower()) - ord("a")): continue
                    newState = ord(grid[x][y]) >= ord("a") and state | 1 << (ord(grid[x][y]) - ord("a")) or state
                    if (newState, x, y) not in memo:
                        memo.add((newState, x, y))
                        heapq.heappush(q, (moves + 1, x, y, newState))
        return -1

    def shortestPathAllKeys_1(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        236ms
        """
        import collections, heapq
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def bfs(grid, source, locations):
            r, c = locations[source]
            lookup = [[False for _ in range(len(grid[0]))]
                      for _ in range(len(grid))]
            lookup[r][c] = True
            q = collections.deque([(r, c, 0)])
            dist = {}
            while q:
                r, c, d = q.popleft()
                if source != grid[r][c] != '.':
                    dist[grid[r][c]] = d
                    continue
                for direction in directions:
                    cr, cc = r + direction[0], c + direction[1]
                    if not ((0 <= cr < len(grid)) and \
                                    (0 <= cc < len(grid[cr]))):
                        continue
                    if grid[cr][cc] != '#' and not lookup[cr][cc]:
                        lookup[cr][cc] = True
                        q.append((cr, cc, d + 1))
            return dist

        locations = {place: (r, c)
                     for r, row in enumerate(grid)
                     for c, place in enumerate(row)
                     if place not in '.#'}
        dists = {place: bfs(grid, place, locations) for place in locations}

        # Dijkstra's algorithm
        min_heap = [(0, '@', 0)]
        best = collections.defaultdict(lambda: collections.defaultdict(lambda: float("inf")))
        best['@'][0] = 0
        target_state = 2 ** sum(place.islower() for place in locations) - 1
        while min_heap:
            cur_d, place, state = heapq.heappop(min_heap)
            if best[place][state] < cur_d:
                continue
            if state == target_state:
                return cur_d
            for dest, d in dists[place].iteritems():
                next_state = state
                if dest.islower():
                    next_state |= (1 << (ord(dest) - ord('a')))
                elif dest.isupper():
                    if not (state & (1 << (ord(dest) - ord('A')))):
                        continue
                if cur_d + d < best[dest][next_state]:
                    best[dest][next_state] = cur_d + d
                    heapq.heappush(min_heap, (cur_d + d, dest, next_state))
        return -1