# -*- coding: UTF-8 -*-
"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
A node in this binary tree can be flipped by swapping the left child and the right child of that node.
Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.
(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)
Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
If we cannot do so, then return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []

Note:
1 <= N <= 100
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        44 ms
        13.3 MB
        """
        """
        实际上如果存在解,只有唯一的解法.按顺序遍历树,如果当前节点不满足voyage的顺序的时候,需要交换左右子树
        如果当前为左子树,则只要有右子树就可以交换,记录位置.若不存在右子树,否则则说明无解.直接返回-1
        如果当前为右子树,则不匹配一定无解,返回-1
        重复上述操作直到返回-1或者遍历整棵树
        """
        ans = []
        cur_voyage = 0

        def dfs(root):
            nonlocal ans, cur_voyage
            # 判断当前节点和目标数目是否一致,不一致说明无解
            if root.val != voyage[cur_voyage]:
                return False
            # voyage向前进
            cur_voyage += 1
            # 如果存在左子树
            if root.left:
                # 不匹配且有右子树,交换两个子树
                if root.left.val != voyage[cur_voyage] and root.right:
                    root.left, root.right = root.right, root.left
                    # 记录交换位置
                    ans.append(root.val)
                # 不匹配不存在右子树,返回-1
                elif root.left.val != voyage[cur_voyage]:
                    return False
                # 匹配则继续进行
                if not dfs(root.left):
                    return False
            # 如果存在右子树
            if root.right:
                # 返回右子树遍历的结果
                return dfs(root.right)
            # 如果顺利进行到叶子节点,返回True
            return True
        # 如果能顺利遍历整棵树,说明有解
        if dfs(root):
            return ans
        # 否则无解
        else:
            return [-1]

    def flipMatchVoyage_1(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        44 ms
        12 MB
        """

        res = []
        self.i = 0

        def dfs(root):
            if not root: return True
            if root.val != voyage[self.i]: return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)

        return res if dfs(root) else [-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().flipMatchVoyage(root, [2, 1]))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().flipMatchVoyage(root, [1, 3, 2]))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().flipMatchVoyage(root, [1, 2, 3]))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().flipMatchVoyage(root, [1, 3, 6, 2, 5, 4]))


