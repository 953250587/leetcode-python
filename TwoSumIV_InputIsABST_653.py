"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        192ms
        """
        dicts={}
        def tree2dict(root,dicts):
            if root==None:
                return None
            if root.val not in dicts.keys():
                dicts[root.val]=1
            else:
                dicts[root.val]+=1
            if root.left!=None:
                dicts=tree2dict(root.left,dicts)
            if root.right!=None:
                dicts=tree2dict(root.right,dicts)
            return dicts
        dicts=tree2dict(root,dicts)
        # print(dicts)
        for i in dicts.keys():
            a=k-i
            if a==i and dicts[i]>=2:
                return True
            elif a!=i and (a in dicts.keys()):
                return True
        return False

    def findTarget_1(self, root, k):
        # 166ms
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False
root=TreeNode(1)
# root.left=TreeNode(3)
# root.right=TreeNode(6)
# root.left.left=TreeNode(2)
# root.left.right=TreeNode(4)
# root.right.right=TreeNode(7)

print(Solution().findTarget(root,2))