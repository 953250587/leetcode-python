"""
 Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        135ms
        """
        if not root:
            return 0
        self.max = -float('inf')
        def dfs(root):
            if not root.left and not root.right:
                self.max = max(self.max, root.val)
                return max(root.val, 0)
            elif root.left and not root.right:
                a = dfs(root.left)
                b = max(a, 0) + root.val
                self.max = max(self.max, b)
                return b
            elif root.right and not root.left:
                a = dfs(root.right)
                b = max(a, 0) + root.val
                self.max = max(self.max, b)
                return b
            else:
                a1 = dfs(root.left)
                a2 = dfs(root.right)
                self.max = max(self.max, max(a1, 0) + max(a2, 0) + root.val)
                return root.val + max(a1, a2, 0)
        dfs(root)
        return self.max

    def maxPathSum_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        global maxpath
        maxpath = -float('inf')
        self.dfs(root)
        return maxpath

    def dfs(self, node):
        global maxpath
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left < 0:  # if left<0, need to cut the left subtree, so left=0
            left = 0
        if right < 0:  # if right<0, need to cut the right subtree, so right=0
            right = 0
        maxpath = max(left + right + node.val, maxpath)
        return max(left, right) + node.val
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().maxPathSum(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(6)
root.left.right = TreeNode(11)
root.right = TreeNode(3)
root.right.right = TreeNode(100)
print(Solution().maxPathSum(None))

root = TreeNode(2)
root.left = TreeNode(-1)
print(Solution().maxPathSum(root))
