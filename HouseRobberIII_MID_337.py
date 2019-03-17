"""
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

     3
    / \
   2   3
    \   \
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        89ms
        """
        if root==None:
            return 0
        self.max_value=0
        self.dicts={}
        def max_rob(root):
            if root.left==None and root.right==None:
                self.dicts[root]=root.val
                self.max_value = max(self.max_value, root.val)
                return
            value = 0
            value_2=0
            if root.left!=None:
                max_rob(root.left)
                value_2+=self.dicts[root.left]
                if root.left.left!=None:
                    value+=self.dicts[root.left.left]
                if root.left.right!=None:
                    value += self.dicts[root.left.right]
            if root.right!=None:
                max_rob(root.right)
                value_2 += self.dicts[root.right]
                if root.right.left!=None:
                    value+=self.dicts[root.right.left]
                if root.right.right!=None:
                    value += self.dicts[root.right.right]
            max_1=max(value+root.val,value_2)
            self.dicts[root]=max_1
            self.max_value=max(self.max_value,max_1)
        max_rob(root)
        print(self.dicts)
        return self.max_value

    def rob_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        65ms
        """
        res = self.dfs(root)
        return res[1]

    def dfs(self, root):
        if not root:
            return (0, 0)
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val))

root=TreeNode(3)
root.left=TreeNode(4)
root.right=TreeNode(5)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print(Solution().rob(None))



