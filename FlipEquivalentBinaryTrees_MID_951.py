"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.



Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram


Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        32 ms
        """
        if not root1 or not root2:
            return not root1 and not root2
        def dfs(root1, root2):
            # 判断根节点的时候数值是否一致
            if root1.val != root2.val:
                return False
            # 没有其它分支结束
            if not root1.left and not root1.right and not root2.left and not root2.right:
                return True
            # 当缺少双方分别缺少左右的时候，左右互换
            if not root1.right and not root2.left and root1.left and root2.right:
                return dfs(root1.left, root2.right)
            if not root1.left and not root2.right and root1.right and root2.left:
                return dfs(root1.right, root2.left)
            # 缺少同一边的时候，保证两边一致
            if not root1.right and not root2.right and root1.left and root2.left:
                return dfs(root1.left, root2.left)
            if not root1.left and not root2.left and root1.right and root2.right:
                return dfs(root1.right, root2.right)
            # 都不缺少的时候，可以换也可以不换
            if root1.left and root1.right and root2.left and root2.right:
                return (dfs(root1.left, root2.right) and dfs(root1.right, root2.left)) \
                       or (dfs(root1.left, root2.left) and dfs(root1.right, root2.right))
            # 否则左右不一致，切不能交换达成，不可能
            else:
                return False

        return dfs(root1, root2)

    def flipEquiv_1(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        40ms
        """
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        else:
            if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) \
                    or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
                return True
            else:
                return False





root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(6)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.right = TreeNode(6)
print(Solution().flipEquiv(root1, root2))