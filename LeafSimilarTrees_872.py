"""

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        24 ms
        """
        def visit_leaf(root, result):
            if not root.left and not root.right:
                result.append(root.val)
                return result
            if root.left:
                result = visit_leaf(root.left, result)
            if root.right:
                result = visit_leaf(root.right, result)
            return result
        a, b = [], []
        a = visit_leaf(root1, a)
        b = visit_leaf(root2, b)
        if len(a) == len(b):
            return all(a[i] == b[i] for i in range(len(a)))
        else:
            return False
