"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        108 ms
        """
        def dfs(root, val):
            if val > root.val:
                if root.right:
                    dfs(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    dfs(root.left, val)
                else:
                    root.left = TreeNode(val)
        dfs(root, val)
        return root

    def insertIntoBST_1(self, root, val):
        """
        100ms
        """
        if not root:
            return False
        elif root.val > val and not self.insertIntoBST(root.left, val):
            root.left = TreeNode(val)
        elif root.val < val and not self.insertIntoBST(root.right, val):
            root.right = TreeNode(val)
        return root