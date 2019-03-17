"""
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        79ms
        """
        if root==None:
            return 0
        def numberOfBinaryTree(root):
            if root.right==None and root.left==None:
                # print("ssad", root.val)
                count_right=0
                count_left=0
                maxsum=0
                return count_right,count_left,maxsum
            if root.right!=None:
                count_right_r,count_left_r,maxsum_right=numberOfBinaryTree(root.right)
                count_right=max(count_right_r,count_left_r)+1
            else:
                maxsum_right=0
                count_right=0
            if root.left!=None:
                count_right_l, count_left_l, maxsum_left = numberOfBinaryTree(root.left)
                count_left=max(count_right_l,count_left_l)+1
            else:
                maxsum_left=0
                count_left=0
            maxsum=max(maxsum_right,maxsum_left)
            maxsum=max(maxsum,count_left+count_right)
            # print(root.val,count_left,count_right)
            return count_right,count_left,maxsum
        return numberOfBinaryTree(root)[2]

    def diameterOfBinaryTree_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        72ms
        """
        self.ans = 0

        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans

def visit(root):
    if root.right != None:
        visit(root.right)
    print(root.val)
    if root.left!=None:
        visit(root.left)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
# visit(root)
print(Solution().diameterOfBinaryTree(root))
