"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        32ms
        """
        if root == None:
            return []
        self.result = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            self.result.append(root.val)
        dfs(root)
        return self.result

    def postorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        35ms
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
print(Solution().postorderTraversal(root))
