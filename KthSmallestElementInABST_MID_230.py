"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        89ms 不加判断102ms
        """
        result=[]
        def add_elment(root):
            if root.left!=None:
                flag=add_elment(root.left)
                if flag:
                    return True
            result.append(root.val)
            if len(result)==k:
                return True
            if root.right!=None:
                flag=add_elment(root.right)
                if flag:
                    return True
            return False
        add_elment(root)
        print(result)
        return result[k-1]

    def kthSmallest_1(self, root, k):
        # 76ms
        stack = [(root, False)]
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    # if visited is True, it means a "small" node is found
                    k -= 1
                    # if k == 0, it means k small nodes has been checked,
                    # the current node is the kth one
                    if k == 0:
                        return curr.val
                else:
                    # Add from right to left
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))
root=TreeNode(1)
root.left=TreeNode(0)
root.right=TreeNode(2)
print(Solution().kthSmallest(root,2))




