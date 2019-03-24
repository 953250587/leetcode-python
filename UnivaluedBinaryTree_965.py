"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false


Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        32 ms
        11.8 MB,
        """
        def bfs(root_list):
            start_val = root_list[0].val
            while root_list:
                next_root_list = []
                for root in root_list:
                    if root.val != start_val:
                        return False
                    if root.left:
                        next_root_list.append(root.left)
                    if root.right:
                        next_root_list.append(root.right)
                root_list = next_root_list
            return True

        if not root:
            return True
        else:
            return bfs([root])

    def isUnivalTree_1(self, root, val=None):
        """
        :type root: TreeNode
        :rtype: bool
        36 ms,
        12MB
        """
        if root is None or root.val == 'null':
            return True
        elif val is None:
            return self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val)
        elif root.val != val:
            return False
        else:
            return self.isUnivalTree(root.left, val) and self.isUnivalTree(root.right, val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(1)
    print(Solution().isUnivalTree(root))

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(1)
    print(Solution().isUnivalTree(root))

