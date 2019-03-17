"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:





We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        108ms
        """
        def dfs(root, deep):
            m = deep
            if root:
                for next_node in root.children:
                    a = dfs(next_node, deep + 1)
                    m = max(m, a)
            return m
        return 0 if not root else dfs(root, 1)