"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        45ms
        """
        dicts={}
        def findfirstright(root,i):
            if i in dicts.keys():
                pass
            else:
                dicts[i] = root.val
            if root.right==root.left==None:
                return None
            if root.right!=None:
                findfirstright(root.right,i+1)
            if root.left!=None:
                findfirstright(root.left,i+1)

        if root == None:
            return []
        findfirstright(root,0)
        return [dicts[i] for i in dicts.keys()]

    def rightSideView_1(self, root):
        res, nxtL= [], [root] if root else []
        while nxtL:
            res.append(nxtL[-1].val) # right most val as to output
            curL, nxtL = nxtL, []
            for i in curL: # build the next level
                if i.left: nxtL.append(i.left)
                if i.right: nxtL.append(i.right)
        return res

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
# root.right.right=TreeNode(4)

print(Solution().rightSideView(root))