"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output:

2

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output:

2

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        778ms
        """
        if root==None:
            return 0
        self.max=-1
        def dp_max(root):
            if root.left==None and root.right==None:
                self.max = max(self.max, 1)
                return 1
            l=0
            r=0
            if root.left!=None:
                l = dp_max(root.left)
            if root.right!=None:
                r = dp_max(root.right)
            print(root.val,l,r)
            if root.left!=None and root.right!=None and \
                            root.val==root.left.val and root.val==root.right.val:
                self.max=max(self.max,1+l+r)
                return 1+max(l,r)
            elif root.left!=None and root.val==root.left.val:
                self.max=max(self.max,1+l)
                return 1+l
            elif  root.right!=None and root.val==root.right.val:
                self.max = max(self.max, 1 + r)
                return 1 + r
            else:
                self.max=max(self.max,1)
                return 1

        dp_max(root)
        return self.max-1

    def longestUnivaluePath_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        709ms
        """

        def dfs(root, res):
            l, r = 0, 0
            if root.left:
                l = dfs(root.left, res)
                l = l + 1 if root.left.val == root.val else 0
            if root.right:
                r = dfs(root.right, res)
                r = r + 1 if root.right.val == root.val else 0
            res[0] = max(res[0], r + l)
            return max(l, r)

        if not root:
            return 0
        res = [0]
        dfs(root, res)
        return res[0]

root=TreeNode(1)
root.left=TreeNode(2)
# root.right=TreeNode(2)
# root.left.left=TreeNode(2)
# root.left.right=TreeNode(2)
# root.right.right=TreeNode(5)
print(Solution().longestUnivaluePath(root))