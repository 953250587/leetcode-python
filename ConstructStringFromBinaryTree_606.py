"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        128ms
        """
        left='';right=''
        if t==None:
            return ''
        if t.right==None and t.left==None:
            return str(t.val)
        if t.left!=None:
            left=self.tree2str(t.left)
        if t.right!=None:
            right=self.tree2str(t.right)
        if right=='':
            ans=str('('+left+')')
        elif left=='':
            ans=str('()'+'('+right+')')
        else:
            ans = str('('+left+')' + '(' + right + ')')
        return str(t.val)+ans

    # 118ms
    def tree2str_1(self, t):
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
# root.left.right=TreeNode(5)
print(Solution().tree2str(root))
