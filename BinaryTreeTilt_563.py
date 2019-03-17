"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        98ms
        """
        if root == None:
            return 0
        def sum_tilt(root):
            if root.right==None and root.left==None:
                sum=0
                val=root.val
                return sum,val
            if root.right!=None:
                sum_r,val_right=sum_tilt(root.right)
            else:
                sum_r=0
                val_right=0
            if root.left!=None:
                sum_l,val_left=sum_tilt(root.left)
            else:
                sum_l=0
                val_left=0
            val=val_left+val_right+root.val
            sum=abs(val_right-val_left)+sum_l+sum_r
            return sum,val
        return sum_tilt(root)[0]

    def findTilt_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        79ms
        """
        self.ans = 0

        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        _sum(root)
        return self.ans

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

print(Solution().findTilt(root))

