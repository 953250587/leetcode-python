"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        68ms
        """
        root = TreeNode(pre[0])
        pre = pre[1:]
        post = post[:-1]

        def dfs(root, pre, post):
            if len(pre) > 0:
                left_val = pre[0]
                right_val = post[-1]
                if left_val == right_val:
                    root.left = TreeNode(left_val)
                    root.left = dfs(root.left, pre[1:], post[:-1])
                else:
                    i, j = 1, -2
                    while pre[i] != right_val:
                        i += 1
                    while post[j] != left_val:
                        j -= 1
                    root.left = TreeNode(left_val)
                    root.left = dfs(root.left, pre[1: i], post[: j])
                    root.right = TreeNode(right_val)
                    root.right = dfs(root.right, pre[i + 1:], post[j + 1 :-1])
            return root
        return dfs(root, pre, post)

    def constructFromPrePost_1(self, pre, post):
        def make(i0, i1, N):
            if N == 0: return None
            root = TreeNode(pre[i0])
            if N == 1: return root

            for L in range(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))
root = Solution().constructFromPrePost(pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1])

def visit(root):
    if root:
        print(root.val)
        visit(root.left)
        visit(root.right)


def visit_1(root):
    if root:
        visit_1(root.left)
        visit_1(root.right)
        print(root.val)

visit(root)
print()
visit_1(root)


