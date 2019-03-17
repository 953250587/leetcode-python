"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        812ms
        """
        if root==None:
            return 0
        max_depth=0
        def countDepth(root,i,max_depth,sum_last):
            if root.left==None and root.right==None:
                flag=True
                max_depth=max(max_depth,i)
                if i<max_depth:
                    flag=False
                else:
                    sum_last+=1
                return flag,sum_last,max_depth
            flag,sum_last,max_depth=countDepth(root.left, i + 1,max_depth,sum_last)
            # print('i:', i, 'max_depth:', max_depth, 'sum_last:', sum_last)
            if not flag:
                return flag, sum_last, max_depth
            if root.right!=None:
                flag, sum_last, max_depth = countDepth(root.right, i + 1,max_depth,sum_last)
            else:
                return False, sum_last, max_depth
            return flag, sum_last, max_depth


        _,sum_leaf,depth=countDepth(root,1,0,0)
        print(_,sum_leaf,depth)
        return 2**(depth-1)-1+sum_leaf

    def countNodes_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l,r,res=root.left,root.right,1
        while l and r:
            res+=res+1
            l,r=l.left,r.right
        if l==r:
            return res
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

root=TreeNode(0)
root.left=TreeNode(1)
root.left.left=TreeNode(2)
# root.left.right=TreeNode(4)
root.right=TreeNode(3)
# root.right.left=TreeNode(5)
# root.right.right=TreeNode(6)
print(Solution().countNodes(root))