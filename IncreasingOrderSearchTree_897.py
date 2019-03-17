"""
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        100 ms
        """
        def dfs(root, value):
            if root:
                value = dfs(root.left, value)
                value.append(root.val)
                value = dfs(root.right, value)
            return value

        value = dfs(root, [])
        head = TreeNode(0)
        copy_head = head
        for i in value:
            root = TreeNode(i)
            head.right = root
            head = head.right

        return copy_head.right

    def increasingBST_1(self, root, tail=None):
        """
        112ms 增加一个参数
        :param root:
        :param tail:
        :return:
        """
        if not root:
            return tail
        res = self.increasingBST_1(root.left, root)
        root.left = None
        root.right = self.increasingBST_1(root.right, tail)
        return res