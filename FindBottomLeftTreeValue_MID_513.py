"""
 Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        63MS
        """
        self.max = -1
        self.result = 0

        def dfs(root, count):
            if root.left:
                dfs(root.left, count + 1)
            else:
                if count > self.max:
                    self.max = count
                    self.result = root.val
            if root.right:
                dfs(root.right, count + 1)

        dfs(root, 0)
        return self.result

    def findBottomLeftValue_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        66MS
        """
        if not root:
            return

        queue = [root]
        while queue:
            root = queue.pop(0)
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
        return root.val

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().findBottomLeftValue(root))

root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(5)
# root.right.left.left = TreeNode(7)
# root.right.right = TreeNode(6)
print(Solution().findBottomLeftValue(root))