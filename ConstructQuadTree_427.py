"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:





The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.



Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
"""

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        L = len(grid)
        def dfs(x, y, l):
            if l == 1:
                if grid[x][y] == 1:
                    return Node(True, True, None, None, None, None)
                else:
                    return Node(False, True, None, None, None, None)
            root = Node(False, False, None, None, None, None)
            root.topLeft = dfs(x, y, l // 2)
            root.topRight = dfs(x, y + l // 2, l // 2)
            root.bottomLeft = dfs(x + l // 2, y, l // 2)
            root.bottomRight = dfs(x + l // 2, y + l // 2, l // 2)
            # print(root.topLeft.val, root.topRight.val)
            # print(l // 2, x, y)
            if root.topLeft.val and root.topRight.val and root.bottomLeft.val and root.bottomRight.val:
                root.isLeaf = True
                root.val = True
                root.topLeft = root.topLeft = root.bottomRight = root.bottomLeft = None
            return root

        return dfs(0, 0, L)

    def construct_1(self, grid):
        """
        200ms
        :param grid:
        :return:
        """
        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                tLeft = dfs(x, y, l // 2)
                tRight = dfs(x, y + l // 2, l // 2)
                bLeft = dfs(x + l // 2, y, l // 2)
                bRight = dfs(x + l // 2, y + l // 2, l // 2)
                value = tLeft.val or tRight.val or bLeft.val or bRight.val
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, tLeft, tRight, bLeft, bRight)
            return node

        return grid and dfs(0, 0, len(grid)) or None
grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
print(Solution().construct(grid))