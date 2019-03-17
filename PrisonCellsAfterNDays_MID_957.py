"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""


class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        52 ms
        """
        key = ''.join(map(str, cells))
        memo = {key: 0}
        memo_num2cell = {0: key}
        count = 0
        while True:
            # 总共只有2**8种可能性，所以必然会开始重复
            next_cells = [0] * 8
            # print('cell:', cells)
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    # print('gg', i)
                    next_cells[i] = 1
            print('cells:', cells, count)
            cells = next_cells
            count += 1
            key = ''.join(map(str, cells))
            if key not in memo:
                memo[key] = count
                memo_num2cell[count] = key
            else:
                basic = memo[key]
                clc = count - basic
                print(basic, clc)
                break
        if N < count:
            return list(map(int, memo_num2cell[N]))
        else:
            return list(map(int, memo_num2cell[(N - count) % clc + basic]))

    def prisonAfterNDays_1(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        44MS
        """
        N -= max(N - 1, 0) / 14 * 14
        for i in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
        return cells


print(Solution().prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], N = 7))
print(Solution().prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], N = 1000000000))
print(Solution().prisonAfterNDays([1,0,1,0,0,0,0,1], 15))



